﻿using System;
using System.Collections.Generic;

namespace Part2
{
    class Program
    {
        static void Main(string[] args)
        {
            List<double> lanternFish = new List<double>(new double[]
            {
                5, 1, 5, 3, 2, 2, 3, 1, 1, 4, 2, 4, 1, 2, 1, 4, 1, 1, 5, 3, 5, 1, 5, 3, 1, 2, 4, 4, 1, 1, 3, 1, 1, 3, 1,
                1, 5, 1, 5, 4, 5, 4, 5, 1, 3, 2, 4, 3, 5, 3, 5, 4, 3, 1, 4, 3, 1, 1, 1, 4, 5, 1, 1, 1, 2, 1, 2, 1, 1, 4,
                1, 4, 1, 1, 3, 3, 2, 2, 4, 2, 1, 1, 5, 3, 1, 3, 1, 1, 4, 3, 3, 3, 1, 5, 2, 3, 1, 3, 1, 5, 2, 2, 1, 2, 1,
                1, 1, 3, 4, 1, 1, 1, 5, 4, 1, 1, 1, 4, 4, 2, 1, 5, 4, 3, 1, 2, 5, 1, 1, 1, 1, 2, 1, 5, 5, 1, 1, 1, 1, 3,
                1, 4, 1, 3, 1, 5, 1, 1, 1, 5, 5, 1, 4, 5, 4, 5, 4, 3, 3, 1, 3, 1, 1, 5, 5, 5, 5, 1, 2, 5, 4, 1, 1, 1, 2,
                2, 1, 3, 1, 1, 2, 4, 2, 2, 2, 1, 1, 2, 2, 1, 5, 2, 1, 1, 2, 1, 3, 1, 3, 2, 2, 4, 3, 1, 2, 4, 5, 2, 1, 4,
                5, 4, 2, 1, 1, 1, 5, 4, 1, 1, 4, 1, 4, 3, 1, 2, 5, 2, 4, 1, 1, 5, 1, 5, 4, 1, 1, 4, 1, 1, 5, 5, 1, 5, 4,
                2, 5, 2, 5, 4, 1, 1, 4, 1, 2, 4, 1, 2, 2, 2, 1, 1, 1, 5, 5, 1, 2, 5, 1, 3, 4, 1, 1, 1, 1, 5, 3, 4, 1, 1,
                2, 1, 1, 3, 5, 5, 2, 3, 5, 1, 1, 1, 5, 4, 3, 4, 2, 2, 1, 3
            });

            int days = 256;
            for (int day = 0; day < days; day++)
            {
                int toAdd = 0;
                for (int i = 0; i < lanternFish.Count; i++)
                {
                    if (lanternFish[i] > 0)
                    {
                        lanternFish[i] -= 1;
                    }
                    else
                    {
                        lanternFish[i] = 6;
                        toAdd++;
                    }
                }

                for (int i = 0; i < toAdd; i++)
                {
                    lanternFish.Add(8);
                }
                
                Console.WriteLine($"Day {day + 1} completed");
            }
            Console.WriteLine(lanternFish.Count);
        }
    }
}