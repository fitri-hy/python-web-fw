from flask import url_for

def render_navbar():
    logo_url = url_for('static', filename='img/logo.png')
    return f'''
    <header class="w-full fixed top-0 flex z-40 justify-between py-4 px-6 bg-white dark:bg-neutral-900 shadow-md items-center">
        <div class="flex gap-2 items-center">
            <img class="h-8 w-8" src="{logo_url}" alt="logo">
            <h1 class="font-bold text-2xl">Py-Framework</h1>
        </div>
        <div class="flex gap-2 items-center">
            <nav class="hidden md:flex gap-4 items-center font-semibold mr-4">
                <a href="/" class="hover:text-blue-600">
                    Home
                </a>
                <a href="/about" class="hover:text-blue-600">
                    About
                </a>
            </nav>
            <button id="theme-toggle" type="button" class="text-amber-500 bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 focus:outline-none rounded-lg text-sm p-2.5">
                <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
                </svg>
                <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path>
                </svg>
            </button>
            <div class="flex md:hidden">
                <button id="menu-button" class="bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 focus:outline-none rounded-lg text-sm p-2.5" aria-expanded="false" aria-controls="sidebar">
                    <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>
            </div>
        </div>
    </header>

    <div id="sidebar" class="fixed z-50 top-0 right-0 h-full w-64 bg-white dark:bg-neutral-900 border-l border-neutral-200 dark:border-neutral-700 shadow-lg sidebar hidden">
        <div class="flex justify-between items-center p-4">
            <h2 class="text-xl font-bold">Menu</h2>
            <button id="close-button" class="text-rose-600 hover:text-rose-500 bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 focus:outline-none rounded-lg text-sm p-2.5">
                <svg class="w-6 h-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
        <div class="w-full flex flex-col gap-1 items-start px-4">
            <a href="/" class="flex w-full p-2 rounded block hover:bg-gray-100 dark:hover:bg-neutral-800">Home</a>
            <a href="/about" class="flex w-full p-2 rounded block hover:bg-gray-100 dark:hover:bg-neutral-800">About</a>
        </div>
    </div>
    '''
