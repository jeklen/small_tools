## debian使用vim的时候碰到了一些问题

### clang_complete: no python support available
可以使用```vim --version```查看
可以发现没有python的features
而在clang_complete.vim中有这样的命令
```
function! s:initClangCompletePython()
  if !has('python')
    echoe 'clang_complete: No python support available.'
    echoe 'Cannot use clang library'
    echoe 'Compile vim with python support to use libclang'
    return 0
  endif
  [..]
```
后来解决方法是安装了vim-nox包，maybe someday i will compile vim myself

### loading libclang failed
我后来是在github的issue中找到了答案
上面有这么一段话
```
no libclang.so in Ubuntu 13.04 but a libclang.so.1,
after symlinking everything worked
```
于是我用软链接解决了问题
```
sudo ln -s /usr/lib/llvm-3.8/lib/libclang.so.1 /usr/lib/libclang.so
```

### vimrc问题解决
github上面有一个很有名的vimrc的库
如何使用：
这个库编辑了.vimrc,讲配置文件的文件夹改掉
然后在里面设置了一些配置文件
个人用户配置可以加在```~/.vim_runtime/my_configs.vim```
