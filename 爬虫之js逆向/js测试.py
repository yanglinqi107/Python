import execjs

# 直接执行
print('execjs.eval：', execjs.eval(' "a、b、c、d、e".split("、") '))

# 先编译、后调用
# 将js文件中的内容读取出来编译即可调用里面的方法了
js_compile = execjs.compile(
    """
    function add(x, y) {
         return x + y;
     }
    """
)

eval_str = "js_compile.call('add', '{}', '{}')".format('abc', 123)
print('eval执行的语句：', eval_str)
print('eval：', eval(eval_str))

print('execjs.compile().call()：', js_compile.call('add', 'abc', 123))