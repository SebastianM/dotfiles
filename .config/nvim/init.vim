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
set smartindent
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
" Hybrid line numbers
set number relativenumber
set nu rnu
" Spell checking
set spell
set spelllang=de_de,en_us
" Enable text wrapping for quick fixes
augroup quickfix
    autocmd!
    autocmd FileType qf setlocal wrap
augroup END

call plug#begin()

" Themes
Plug 'joshdick/onedark.vim'
Plug 'vim-airline/vim-airline'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'unblevable/quick-scope'
Plug 'sheerun/vim-polyglot'
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'mhinz/vim-startify'
Plug 'mattn/emmet-vim'
Plug 'prettier/vim-prettier', { 'do': 'npm install' }
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'Raimondi/delimitMate'
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

" Transparency support
Plug 'miyakogi/seiya.vim'

call plug#end()

" Plugin configs
source ~/.config/nvim/plugins/coc.vim
source ~/.config/nvim/plugins/startify.vim
source ~/.config/nvim/plugins/quickscope.vim

" Transparency support
let g:seiya_auto_enable=1

" Key bindings
nnoremap <silent> <C-p> <cmd>Telescope find_files<cr>
" nnoremap <silent> <C-p> :GFiles<CR>
nnoremap <silent> <C-n> :CocCommand explorer<CR>
nnoremap <silent> <C-K> :GoImports<CR>:GoBuild<CR>
" nnoremap <silent> == :Buffers<CR>
nnoremap <silent>== <cmd>Telescope buffers<cr>
nnoremap <silent> ?? <cmd>Telescope live_grep<CR>

noremap <silent> <C-S-Left> :vertical resize -1<CR>
noremap <silent> <C-S-Right> :vertical resize +1<CR>
