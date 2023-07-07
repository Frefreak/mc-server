### 整合包信息

当前: Multiblock Madness 2 (MBM2)

版本: 0.2.3

- [curseforge](https://www.curseforge.com/minecraft/modpacks/multiblock-madness-2)
- [mcmod](https://www.mcmod.cn/modpack/583.html)

### ftbquests汉化相关(必看)

因为要让ftbquests支持多语言，修改了服务器的`config/ftbquests/quests`目录，客户端需
要将相应的语言文件加到客户端里。

- 需要任务文本为英文，下载[en\_us.json](mbm2/en_us.json)
- 需要任务文本为中文，下载[en\_us.json](mbm2/en_us.json)和[zh\_cn.json](mbm2/zh_cn.json)

下载后将json文件放置到`/path/to/minecraft/kubejs/assets/<name>/lang`目录中，重启游戏即可。

`<name>`可以是任意合法名，不要覆盖现有的，新建`/<name>/lang`目录。
示例：![](e6e/e6e_lang.png)

这个改动只影响服务器游玩，单机不会有影响。
