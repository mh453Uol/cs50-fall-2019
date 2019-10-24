#include "helpers.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // 1. iterate through each row of the image
    // 2. get the current pixel
    //  2.1 BGR i.e 0x{ff}{99}{00}
    //                  B   G   R
    // Black (0x00 [0]) - White (0xff [255])
    // Higher value i.e 230,220,100 means lighert
    // Lower value i.e 10,1,2 means dark
    //  3. for each pixel do BGR/3
    //      3.1 255,255,255 = 255*3/3 = 255
    //      3.2 0,0,0 = 0*3 = 0/3 = 0
    //      3.3 230,220,100 = 550/3 = 183.33 so 183
    //      3.4 10,1,2 = 13/3 = 4.33 so 4
    RGBTRIPLE pixel;
    int average = 0;
    for(int h = 0; h < height; h++) {
        for(int w = 0; w < width; w++) {
            pixel = image[h][w];
            average = round(((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue)/3.0));
            image[h][w].rgbtRed = average;
            image[h][w].rgbtGreen = average;
            image[h][w].rgbtBlue = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // 1. iterate each row
    // 2. for each pixel do
    //  2.1 red = 0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue
    //  2.2 green = 0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue
    //  2.3 blue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    // 3. round all red, green, blue
    // 4. if red,green,blue > 255 then set to 255
    RGBTRIPLE pixel;
    int sepiaRed = 0;
    int sepiaGreen = 0;
    int sepiaBlue = 0;

    for(int h = 0; h < height; h++) {
        for(int w = 0; w < width; w++) {
            pixel = image[h][w];
            sepiaRed = round(.393 * pixel.rgbtRed + .769 * pixel.rgbtGreen + .189 * pixel.rgbtBlue);
            sepiaGreen = round(.349 * pixel.rgbtRed + .686 * pixel.rgbtGreen + .168 * pixel.rgbtBlue);
            sepiaBlue = round(.272 * pixel.rgbtRed + .534 * pixel.rgbtGreen + .131 * pixel.rgbtBlue);

            if(sepiaRed > 255) {
                sepiaRed = 255;
            }
            if(sepiaGreen > 255) {
                sepiaGreen = 255;
            }
            if(sepiaBlue > 255) {
                sepiaBlue = 255;
            }

            image[h][w].rgbtRed = sepiaRed;
            image[h][w].rgbtGreen = sepiaGreen;
            image[h][w].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //1. iterate through each pixel width = 100
    //2. h=0,w=0 -> h=0,w=100 (top left should be moved to top right)
    //  2.1 h=0,w=1 -> h=0,w=99
    //  2.2 h=0,w=2 -> h=0,w=98
    //  ...
    //  2.3 h=0,w=98 -> h=0,w=2
    //  2.4 h=0,w=99 -> h=0,w=1
    //3. for each pixel current position = absolute(current ith index in row - width)
    int currentPixelRed;
    int currentPixelGreen;
    int currentPixelBlue;

    int oppositePixelRed;
    int oppositePixelGreen;
    int oppositePixelBlue;
    int oppositePixelWidthIndex = 0;

    RGBTRIPLE(*originalImage)[width] = image;

    int middleOfImage = round(width/2);

    for(int h = 0; h < height; h++) {
        for(int w = 0; w < middleOfImage; w++) {
            oppositePixelWidthIndex = abs(w - (width - 1));

            currentPixelRed = image[h][w].rgbtRed;
            currentPixelGreen = image[h][w].rgbtGreen;
            currentPixelBlue = image[h][w].rgbtBlue;

            oppositePixelRed = image[h][oppositePixelWidthIndex].rgbtRed;
            oppositePixelGreen = image[h][oppositePixelWidthIndex].rgbtGreen;
            oppositePixelBlue = image[h][oppositePixelWidthIndex].rgbtBlue;

            image[h][oppositePixelWidthIndex].rgbtRed = currentPixelRed;
            image[h][oppositePixelWidthIndex].rgbtGreen = currentPixelGreen;
            image[h][oppositePixelWidthIndex].rgbtBlue = currentPixelBlue;

            image[h][w].rgbtRed = oppositePixelRed;
            image[h][w].rgbtGreen = oppositePixelGreen;
            image[h][w].rgbtBlue = oppositePixelBlue;

        }
    }
}

bool isInsideImageBoundary(int currentRow, int currentColumn, int height, int width) {
    return (currentRow >= 0 && currentRow < height) && (currentColumn >= 0 && currentColumn < width);
}
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // 1. iterate over each pixel
    // 2. use box blue technique
    //  2.1 | 1  | 2  | 3  | 4  |
    //      | 5  | 6  | 7  | 8  |
    //      | 9  | 10 | 11 | 12 |
    //      | 13 | 14 | 15 | 16 |
    //  2.2 pixel 10 - get average of (3x3 matrix) so average of 5,6,7,9,10,11,13,14,15
    //  2.3 pixel 15 (on edge) - get average of (3x3 matrix) so average of 10,11,12,14,15,16
    //  2.4 get 3x3 matrix = current row - 1, 0, row +1
    //      i.e pixel 15 | row = 3 so 13-1=12 (top), 13 (middle), 14 (bottom)

    float pixelsInBlurBox = 0.0;
    int blurBoxTotalRedPixel = 0;
    int blurBoxTotalGreenPixel = 0;
    int blurBoxTotalBluePixel = 0;

    int currentRow = 0;
    int currentColumn = 0;

    RGBTRIPLE originalImage[height][width];

    // create copy of the original image
    for(int h = 0; h < height; h++) {
        for(int w = 0; w < width; w++) {
            originalImage[h][w] = image[h][w];;
        }
    }

    RGBTRIPLE pixel;
    for(int h = 0; h < height; h++) {
        for(int w = 0; w < width; w++) {
            // (-1,-1) (-1,0) (-1,1)
            // (0,-1) (0,0) (0,1)
            // (1,-1) (1,0) (1,1)
            // (3x3 matrix)
            //printf("Pixel: (%d,%d) \n",h,w);
            for(int row = -1; row < 2; row++) {
                for(int column = -1; column < 2; column++) {
                    currentRow = h + row;
                    currentColumn = w + column;

                    if(isInsideImageBoundary(currentRow,currentColumn,height,width) == true)
                    {
                        pixel = originalImage[currentRow][currentColumn];
                        blurBoxTotalRedPixel += pixel.rgbtRed;
                        blurBoxTotalGreenPixel += pixel.rgbtGreen;
                        blurBoxTotalBluePixel += pixel.rgbtBlue;

                        pixelsInBlurBox++;
                        //printf("In boundary: (%d,%d) \t",currentRow,currentColumn);
                    } else {
                        //printf("Out boundary:(%d,%d) \t",currentRow,currentColumn);
                    }
                }
                //printf("\n");
            }
            image[h][w].rgbtRed = round(blurBoxTotalRedPixel / pixelsInBlurBox);
            image[h][w].rgbtGreen = round(blurBoxTotalGreenPixel / pixelsInBlurBox);
            image[h][w].rgbtBlue = round(blurBoxTotalBluePixel / pixelsInBlurBox);

            pixelsInBlurBox = 0.0;
            blurBoxTotalRedPixel = 0;
            blurBoxTotalGreenPixel = 0;
            blurBoxTotalBluePixel = 0;
            //printf("-------------------------------------\n");
        }
    }
}
