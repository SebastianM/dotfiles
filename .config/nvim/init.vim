" general settings

syntax on
colorscheme onedark
set background=dark
set nu
filetype plugin indent on
set nocp
set ruler
set wildmenu
set t_Co=256
set mouse=a
"Code folding
set foldmethod=manual
"Tabs and spacing
set autoindent
set cindent
set tabstop=4
set expandtab
set shiftwidth=4
set smarttab
"Search
set hlsearch
set incsearch
set ignorecase
set smartcase
set diffopt +=iwhite


call plug#begin()

" Themes
Plug 'joshdick/onedark.vim'
Plug 'vim-airline/vim-airline'


Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'mhinz/vim-startify'

" Transparency support
Plug 'miyakogi/seiya.vim'

call plug#end()

source ~/.config/nvim/plugins/coc.vim
source ~/.config/nvim/plugins/startify.vim

" Transparency support
let g:seiya_auto_enable=1


" Key bindings
nnoremap <silent> <C-p> :Files<CR>
nnoremap <silent> <C-P> :GFiles<CR>
