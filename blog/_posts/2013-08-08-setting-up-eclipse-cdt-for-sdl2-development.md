---
layout: post
title: Setting up Eclipse CDT for SDL2 development
categories:
- eclipse
- gamedev
tags:
- C++
- SDL2
status: publish
type: post
published: true
meta:
  geo_public: '0'
  _wpas_mess: Setting up Eclipse CDT for SDL2 development http://wp.me/p2qXd0-1F
  _publicize_pending: '1'
  _elasticsearch_indexed_on: '2013-08-08 13:00:25'
  _wpas_done_1297749: '1'
  _publicize_done_external: a:1:{s:8:"facebook";a:1:{i:90410736;b:1;}}
  publicize_twitter_user: zxiiro
  _wpas_done_757240: '1'
  _wpas_done_757239: '1'
  _wpas_skip_1297749: '1'
  _wpas_skip_757240: '1'
  _wpas_skip_757239: '1'
---
This tutorial assumes you already have SDL2 installed. If your on Linux install it using your Distro's package manager. On OpenSUSE you can find SDL2 in the Games repository, details can be found here http://en.opensuse.org/Games

First you'll want a copy of Eclipse for C/C++ Developers from http://www.eclipse.org/downloads/

Once downloaded you'll want to unzip it somewhere on your harddrive. I'm on Linux so I unzipped it to /home/myuser/apps/

Launch Eclipse, it will ask you to pick a workspace. I just leave it the defaults and move on.

Create a new c++ project (File &gt; New &gt; C++ Project). You will need to pick a toolchain, I'm on Linux so I picked Linux GCC.

Before you can build your project there is a few things you will need to configure.

- If you want to use c++11 do the following:

1. Right click your Project under "Package Explorer" and select Properties.
2. Select (C/C++ Build &gt; Settings &gt; GCC C++ Compiler &gt; Miscellaneous)
3. Under "Other flags" add: <strong>-std=c++0x</strong>
4. Click Apply then OK

- Configure Eclipse to use SDL2

1. Right click your Project under "Package Explorer" and select Properties.
2. Select (C/C++ General &gt; Paths and Symbols &gt; Libraries)
3. Click "Add" and add "SDL2" and click OK
4. Click "Add" and add "SDL2main" and click OK

Your project should be configured for SDL2 development now. Lets try creating a quick Hello World program just to make sure.

Create a main.cpp file and add the following code.

{% highlight cpp %}
#include "SDL2/SDL.h";

int main(int argc, char** argv){

    // Start SDL2
    SDL_Init(SDL_INIT_EVERYTHING);

    // Create a Window in the middle of the screen
    SDL_Window *window = nullptr;
	window = SDL_CreateWindow("Hello World!",
			SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, // x and y
			640, 480, // Width and Height
			SDL_WINDOW_SHOWN);

    // Delay so that we can see the window appear
    SDL_Delay(2000);

    // Cleanup and Quit
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
{% endhighlight %}

You should now be able to build and run this code.

To build press <strong>ctrl+b</strong>.
To run press <strong>ctrl+f11</strong>.

A blank window should appear with the title "Hello World!". If you see this congratulations you've successfully configured SDL2 in Eclipse.
