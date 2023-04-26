### 整合包信息

当前: GTNH 2.3.3

- [官方安装说明](https://gtnh.miraheze.org/wiki/Installing_and_Migrating)
- [官方wiki](https://gtnh.miraheze.org/wiki/Main_Page)
- [curseforge](https://www.curseforge.com/minecraft/modpacks/gt-new-horizons)
- [mcmod](https://www.mcmod.cn/modpack/1.html)

### 额外mod

除本体外还需要安装如下mod才可进入服务器。

- [FTBLib-1.0.19](https://github.com/GTNewHorizons/FTB-Library/releases/tag/1.0.19-GTNH): FTBUtilities的依赖。[下载地址](https://github.com/GTNewHorizons/FTB-Library/releases/download/1.0.19-GTNH/FTBLib-1.0.19-GTNH.jar)
- [FTBUtilities-1.0.19](https://github.com/GTNewHorizons/FTB-Library/releases/tag/1.0.19-GTNH): chunk loader, 区块保护等。[下载地址](https://github.com/GTNewHorizons/FTB-Library/releases/download/1.0.19-GTNH/FTBLib-1.0.19-GTNH.jar)

### changelog

- **2.3.2** -> **2.3.3**: [changelog](gtnh/changelog_from_2.3.2_to_2.3.3.md)

### curseforge包使用高版本java启动

如果是以启动器直接下载的curseforge包，可以参考[lwjgl3ify](https://github.com/GTNewHorizons/lwjgl3ify)的README来使用高版本java启动。

以下是客户端部分翻译(AI):

------------

要在 PrismLauncher 或 MultiMC 中安装：

将 `lwjgl3ify-VERSION-multimc.zip` 的内容复制到 `instances/My Modpack/`。
需要覆盖 `mmc-pack.json`。 重新加载启动器，在实例窗口中应显示修改过的 Forge、
Minecraft 和 LWJGL3 版本。 将 mod jar（`lwjgl3ify-VERSION.jar`）放在实例的
minecraft 文件夹中的 `mods/`，它将作为核心模组加载。 forgePatches jar
将由启动器自动下载。

将实例的 Java 版本更改为 17.0.6（或更新版本）、19.0.2（或更新版本）或 20（或更新版本），这些是当前支持的版本。 如果从 patches/me.eigenraven.lwjgl3ify.forgepatches.json 中删除 `-Djava.security.manager=allow` 参数，您还可以使用 Java 11。

对于 MultiMC，您需要手动输入额外的 Java 参数，prismlauncher 可以从补丁 json 文件自动加载它们：

```
--illegal-access=warn -Djava.security.manager=allow -Dfile.encoding=UTF-8 --add-opens java.base/jdk.internal.loader=ALL-UNNAMED --add-opens java.base/java.net=ALL-UNNAMED --add-opens java.base/java.nio=ALL-UNNAMED --add-opens java.base/java.io=ALL-UNNAMED --add-opens java.base/java.lang=ALL-UNNAMED --add-opens java.base/java.lang.reflect=ALL-UNNAMED --add-opens java.base/java.text=ALL-UNNAMED --add-opens java.base/java.util=ALL-UNNAMED --add-opens java.base/jdk.internal.reflect=ALL-UNNAMED --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens jdk.naming.dns/com.sun.jndi.dns=ALL-UNNAMED,java.naming --add-opens java.desktop/sun.awt.image=ALL-UNNAMED --add-modules jdk.dynalink --add-opens jdk.dynalink/jdk.dynalink.beans=ALL-UNNAMED --add-modules java.sql.rowset --add-opens java.sql.rowset/javax.sql.rowset.serial=ALL-UNNAMED
```

如果您想调整默认窗口大小、OpenGL上下文属性或其他更高级的设置，请在首次启动后查看`config/lwjgl3ify.cfg`中的配置文件。

-----------------
