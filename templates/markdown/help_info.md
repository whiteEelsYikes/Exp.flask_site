# Exp(实验室)帮助信息

---

##  局域网 https ssl 验证 无效（网站不安全问题）：

原因：

- 因为网站的`wsgi`服务是设置开启了`ssl`加密  就是只能使用`https`访问
- 其实 服务器还使用了`nginx`做反向代理
- 主要是因为没有 完整`https`+`CA证书`验证 所以会提示：不安全

解决方法：

这里提供一个文件按要求操作文件就可以解决访问网站提示不安全问题

[![下载 图标](./static/markdown_images/help_info.images/Downloads_29996-1693616983169-3.png)下载文件]( ../static/file/192.168.9.99.zip)

文件下载完成以后将其解压，然后`cmd` 或`pshell`在解压的目录下执行命令：

```shell
./mkcert-v1.4.4-windows-amd64.exe -install
```

命令执行完毕以后应该是没有问题了，重启浏览器再次访问正常情况应该是可以正常访问了，`https`验证应该也没有问题了

---

## 维护问题：

这个网站或许会继续更新（但更新维护速度会非常缓慢）但也许就停更了，后端还有很多东西可能没有做完，web前端就无所谓了，我也不是很懂这东西

[![example](https://img.shields.io/badge/Exp.flask_site-GitHub-blue.svg)前往Github查看项目](https://github.com/whiteEelsYikes/Exp.flask_site)

---













