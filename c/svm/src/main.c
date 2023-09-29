#include <stdio.h>
#include <stdbool.h>
#include <SDL.h>

#include "library_math.h"
#include "library.h"
#include "full_connected.h"
#include "print.h"


#define title "SVM"
#define window_width 16 * 65
#define window_height 9 * 65


typedef struct Point {
    int x, y, type;
} Point;

typedef struct Color {
    int r, g, b, a;
} Color;


int init();
void quit();
void add_point();
void draw_circle(double x, double y, double radius, Color* color);
void draw_borderedCircle(double x, double y, double radius, double border, Color* color, Color* border_color);
void draw_type_border(int border_size);


SDL_Window* window;
SDL_Renderer* renderer;
SDL_Event event;

int length = 0;
Point* points;

int types_count = 2;
Color** type_colors;

int x, y;
int type = 0;


int main(int argc, char* argv[]) {
    if (init() != 0) {
        return 1;
    }

    points = (Point *)malloc(sizeof(Point) * length);
    type_colors = (Color**)malloc(sizeof(Color*) * types_count);

    type_colors[0] = (Color*)malloc(sizeof(Color));
    type_colors[0]->r = 220;
    type_colors[0]->g = 40;
    type_colors[0]->b = 55;
    type_colors[0]->a = 255;

    type_colors[1] = (Color*)malloc(sizeof(Color));
    type_colors[1]->r = 30;
    type_colors[1]->g = 230;
    type_colors[1]->b = 38;
    type_colors[1]->a = 255;

    Color* border_color = (Color*)malloc(sizeof(Color));
    border_color->r = 40;
    border_color->g = 40;
    border_color->b = 40;
    border_color->a = 255;


    DataSet *train_set = DataSet_construct(0, 2, 2, (double []){
        //  input       output
    });

    int layers[] = {2, 4, types_count};
    int *ptr_layers = layers;

    FullConnected *layer = FullConnected_construct(3, ptr_layers, 0.5, 0.3);
    FullConnected_train_construct(layer);

    bool run = true;

    while (run) {
        while(SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                run = false;
                break;
            }
            if (event.type == SDL_KEYDOWN) {
                if (event.key.keysym.sym == SDLK_ESCAPE) {
                    run = false;
                    break;
                }
                if (event.key.keysym.sym == SDLK_1) {
                    type -= 1;
                    if (type < 0) {
                        type = types_count - 1;
                    }
                }
                if (event.key.keysym.sym == SDLK_2) {
                    type += 1;
                    if (type >= types_count) {
                        type = 0;
                    }
                }
                if 
            }
            if (event.type == SDL_MOUSEBUTTONDOWN) {
                if (event.button.button == SDL_BUTTON_LEFT) {
                    SDL_GetMouseState(&x, &y);
                    add_point();
                    if (type == 0) {
                        DataSet_add(train_set, (double[]){x / window_width, y / window_height, 1, 0});
                    } else {
                        DataSet_add(train_set, (double[]){x / window_width, y / window_height, 0, 1});
                    }
                }
            }
        }

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderClear(renderer);

        for (int i = 0; i < length; ++i) {
            draw_borderedCircle(points[i].x, points[i].y, 15, 3, type_colors[points[i].type], border_color);
        }

        draw_type_border(5);

        SDL_RenderPresent(renderer);
    }

    free(points);
    for (int i = 0; i < types_count; ++i) {
        free(type_colors[i]);
    }
    free(type_colors);
    free(border_color);

    FullConnected_train_deconstruct(layer);
    FullConnected_deconstruct(layer);

    DataSet_deconstruct(train_set);

    quit();

    return 0;
}


int init() {
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        printf("!!! ERROR in SDL_Init() !!!\n%s", SDL_GetError());
        return 1;
    }

    window = SDL_CreateWindow(title, 100, 100, window_width, window_height, SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("!!! ERROR in SDL_CreateWindow() !!!\n%s", SDL_GetError());
        return 1;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (renderer == NULL) {
        printf("!!! ERROR in SDL_CreateRenderer() !!!\n%s", SDL_GetError());
        return 1;
    }

    return 0;
}


void quit() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}


void add_point() {
    length += 1;
    points = (Point *)realloc(points, length * sizeof(Point));
    points[length - 1].x = x;
    points[length - 1].y = y;
    points[length - 1].type = type;
}


void draw_circle(double x, double y, double radius, Color* color) {
    SDL_SetRenderDrawColor(renderer, color->r, color->g, color->b, color->a);
    for (int xi = x - radius; xi <= x + radius; ++xi) {
        for (int yi = y - radius; yi <= y + radius; ++yi) {
            if ( (xi - x) * (xi - x) + (yi - y) * (yi - y) <= radius * radius ) {
                SDL_RenderDrawPoint(renderer, xi, yi);
            }
        }
    }
}


void draw_borderedCircle(double x, double y, double radius, double border, Color* color, Color* border_color) {
    draw_circle(x, y, radius, border_color);
    draw_circle(x, y, radius - border, color);
}


void draw_type_border(int border_size) {
    SDL_SetRenderDrawColor(renderer, type_colors[type]->r, type_colors[type]->g, type_colors[type]->b, type_colors[type]->a);
    for (int i = 0; i < border_size; ++i) {
        for (int x = i; x < window_width - i; ++x) {
            SDL_RenderDrawPoint(renderer, x, i);
            SDL_RenderDrawPoint(renderer, x, window_height - i - 1);
        }
        for (int y = i; y < window_height - i; ++y) {
            SDL_RenderDrawPoint(renderer, i, y);
            SDL_RenderDrawPoint(renderer, window_width - i - 1, y);
        }
    }
}
