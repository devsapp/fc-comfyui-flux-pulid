
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# fc-comfyui-flux-pulid 帮助文档

<description>

部署 ComfyUI + Flux Pulid 到阿里云函数计算

</description>

<codeUrl>



</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>

| 服务 |  备注  |
| --- |  --- |
| 函数计算 FC |  提供 CPU、GPU 等计算资源 |
| 文件存储 NAS |  存储大模型文件 |

</service>


<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-comfyui-flux-pulid) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-comfyui-flux-pulid) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://docs.serverless-devs.com/user-guide/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://docs.serverless-devs.com/user-guide/install) ，并进行[授权信息配置]( https://docs.serverless-devs.com/user-guide/config) ；
  - 初始化项目：`s init fc-comfyui-flux-pulid -d fc-comfyui-flux-pulid`
  - 进入项目，并进行项目部署：`cd fc-comfyui-flux-pulid && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例展示了如何将 PuLID for FLUX 部署到阿里云函数计算上，从而在云端体验人像写真的换脸效果。

Flux 是由 Black Forest Labs 推出的文生图模型，其在文本控制、绘图质量、排版能力等多方面已经超越了包括 Midjourney、Stable Diffusion 等常用的文生图模型。

PuLID for Flux 是一个优秀的AI 头像生成项目，它提供了一种无需训练 LoRA 就能实现面部迁移信息保持的方法。这个项目特别适合用于 FLUX.1-dev 模型，能够生成人脸高度一致性的风格化图像 。PuLID for Flux 的使用场景非常广泛，包括但不限于艺术创作、虚拟形象定制、影视制作、广告与营销以及社交媒体等 。它能够提供逼真的面部定制，保持原始风格，支持个性化编辑，并且能够快速生成图像，无需复杂的模型调整或参数优化 。

ComfyUI 是一个为 Stable Diffusion 模型设计的，功能强大且高度模块化的图形用户界面（GUI）。它允许用户基于节点构建 AIGC 创作流程，非常适合那些想要摆脱传统编程方法、采用更直观操作流程的用户。该工具由 Comfyanonymous 在 2023 年 1 月创建，初衷是深入了解 Stable Diffusion 模型的运作机制。由于其易用性，Stable Diffusion 的开发者 Stability AI 也采用了 ComfyUI 进行内部测试，并聘请 Comfyanonymous 协助开发内部工具。目前，ComfyUI 在 Github 上的 Fork 数超过 3000，Star 数超过 30000。

ComfyUI 提供了方便的能力使用 Flux 进行文本绘图。通过 Serverless 开发平台，您只需要几步，就可以基于 Flux 体验 Comfyui，并享受Serverless 架构带来的降本提效的技术红利。

</appdetail>

## 使用流程

<usedetail id="flushContent">

### 创建并部署Flux模型

1. 打开 FC 应用中心，选择“人工智能”Flux Pulid 换脸，单击立即创建。

![](https://img.alicdn.com/imgextra/i2/O1CN01JrRhZS1WqlpKgsP5F_!!6000000002840-0-tps-2517-983.jpg)

2. 在创建应用页面，点击“创建应用”

3. 等待约1分钟，部署状态变为部署成功，表示应用部署成功，并生成访问域名，单击访问域名后的链接，开始体验 Flux 大模型生图。

![](https://img.alicdn.com/imgextra/i4/O1CN01O921Td1tU5NCalcbu_!!6000000005904-0-tps-1536-878.jpg)

**注意**
  - 请注意保护域名的安全，不要泄露给其他人，防止产生额外费用。
  - `***.devsapp.net`域名是 CNCF SandBox 项目 Serverless Devs 社区所提供，仅供学习和测试使用，不可用于任何生产使用；社区会对该域名进行不定期地拨测，并在域名下发30天后进行回收，强烈建议您绑定自定义域名以获得更好的使用体验。

4. 首次打开ComfyUI，遇到无法访问此网站情况，等待10 秒左右单击重新加载。

![](https://img.alicdn.com/imgextra/i3/O1CN01Atdvpe27tBhYRpKQb_!!6000000007854-0-tps-1324-752.jpg)



### ComfyUI+Flux+Pulid 实现换脸写真

1.  访问下方链接，下载预置的 json文件（如果看到为代码，可直接复制全部代码，粘贴到ComfyUI 中即可）[workflow.json](https://aliyuque.antfin.com/raw?filekey=lark%2F0%2F2024%2Fjson%2F168324%2F1729131998221-6e7c3195-620e-4eba-b6e9-5d67310c6bfd.json&from=https%3A%2F%2Faliyuque.antfin.com%2Fite309%2Fqhifem%2Fnge05g9540ns2ph8%2Fedit%2304d483b2ccm2m)

2. 在页面右下角，单击Load，将下载并解压后的json文件导入到 ComfyUI 中。

![](https://img.alicdn.com/imgextra/i4/O1CN01BDN1sU1lWMPmVrOzh_!!6000000004826-0-tps-703-567.jpg)

![](https://img.alicdn.com/imgextra/i4/O1CN01my25wX1WxdlhA4p2V_!!6000000002855-0-tps-1619-1226.jpg)

3. 点击“choose file to upload” 上传本地的人像图片

![](https://img.alicdn.com/imgextra/i2/O1CN01sQ3SFQ1rwMayXRCN9_!!6000000005695-0-tps-825-405.jpg)

4. 在页面右下方，直接单击 Queue Prompt，通过默认的提示词生成图像

![](https://img.alicdn.com/imgextra/i2/O1CN01vfhNdB1NKPIZMHi5y_!!6000000001551-0-tps-688-541.jpg)

> 重要：由于ComfyUI自身需要长久保持WebSocket连接以同步实时状态，因此页面打开时会持续使用计算资源，即页面打开就会有费用产生请您在不使用ComfyUI的时候关闭页面，如果不进行主动操作，页面也会在 10 分钟后自动关闭，以节省您的费用。

5. 因为 ComfyUI 基于 Serverless 函数计算产品部署，因此生成第一张图的时候需要冷启动时间，第一张图生成需要等待 5 分钟左右，后续每张图生成时间为 2-5 秒。

![](https://img.alicdn.com/imgextra/i3/O1CN01pPCwPo1lxNma8CPeS_!!6000000004885-0-tps-720-334.jpg)

![](https://img.alicdn.com/imgextra/i4/O1CN01yVmCQN1vSpWFJedEY_!!6000000006172-0-tps-720-410.jpg)

6. 您可以通过修改“提示词”生成更多风格

![](https://img.alicdn.com/imgextra/i1/O1CN01iLZp1g1yzIRTsGnnu_!!6000000006649-0-tps-2227-454.jpg)

您也可以使用下面示例图片体验效果（以下图片为 AI 生成）

![](https://img.alicdn.com/imgextra/i4/O1CN010j9e991TYxZwmqHgn_!!6000000002395-0-tps-949-697.jpg)

女生可选:
提示词1：Half-body portrait of a young woman with an expression of awe and fascination, immersed in the intricate web of AI algorithms and data streams, surrounded by sleek laptops and a nest of charging cables. Her blouse bears the words "AI Enthusiast" in an elegant script font, reflecting her passion for artificial intelligence. The background is a soft glow, reminiscent of a well-lit workspace, with a photorealistic touch that adds depth to the scene. Her skin is depicted with natural imperfections, capturing the essence of a candid smartphone snapshot, yet with the detail and texture that suggest the use of a high-quality camera. The image conveys a realistic, non-glamorized portrayal of her features, with an laptop prominently displayed in the corner, indicating her tech-savvy persona.

提示词2: Half-body portrait of a young girl with an expression of curiosity and excitement, immersed in the digital world of virtual reality, surrounded by high-tech augmented reality glasses and floating holographic screens, her sweatshirt printed with the words "Future Explorer" in a stylish font, the background filled with dynamic data streams and galaxy-like speckles of light, featuring a futuristic style, with photorealistic details and natural skin texture, as if shot with a high-end smartphone, the skin details are authentic and not artificial, with an laptop placed beside her.

男生可选：
提示词1: Half-body portrait of a young man with a focused and confident smile, surrounded by the glow of encoded matrices and programming languages, with multiple coding monitors and a tangle of data cables around him, his T-shirt printed with "Code Master" in a clean sans-serif font, the background displaying the radiance of digital circuits and optical fibers, featuring a cyberpunk style, with photorealistic visual effects, clear skin texture, as if captured with a professional camera, the skin details are realistic and tactile, with a mechanical keyboard placed beside him.

提示词2: Half-body portrait of a young man with a gaze that is resolute and brimming with passion, encircled by the halo of innovative technology, surrounded by multiple touch-screen monitors displaying intricate algorithms and system architectures, as well as a maze of data cables and charging wires. He dons a T-shirt imprinted with "Tech Pioneer" in modern, minimalist font, symbolizing his vanguard status in the realm of technology. The background flickers with the indicator lights of smart devices and flowing lines of code, presenting a science fiction style with a tinge of futurism. The image is rendered with photographic realism, skin textures are clearly visible, as if meticulously captured with a professional camera, with details so authentic they eschew any plastic appearance. Beside him lies gaming mouse, hinting at his love and pursuit of high-performance technology.

您也可以通过 [通义](https://tongyi.aliyun.com/qianwen/) 或者其他AI大语言模型生成其他提示词，尝试其他生图效果

![](https://img.alicdn.com/imgextra/i4/O1CN01eNLsRV1j0BLznfrj9_!!6000000004485-0-tps-1125-689.jpg)


</details>

</usedetail>

## 注意事项

<matters id="flushContent">

fc-comfyui 是一个第三方工具，旨在帮助用户将 ComfyUI 项目部署到阿里云函数计算服务。请注意，该工具与 ComfyUI 项目及阿里云官方无直接联系。

- **第三方链接**：本工具提供的第三方网站或服务链接仅为用户方便，开发者对这些内容、隐私政策或操作不承担责任，亦不代表认可。
- **社区同步**：ComfyUI 为活跃的开源社区项目，功能丰富且更新频繁，如果您希望使用更新版本的 ComfyUI，可自行基于 Dockerfile 文件进行构建。
- **费用提示**：在阿里云部署 ComfyUI 可能产生费用，请参考阿里云的计费文档。若需持久化存储（如模型、节点），还需开通文件管理 NAS，可能产生额外费用。
- **许可协议**：使用 ComfyUI 项目需遵守其开源许可协议。使用前，请确保已阅读并理解 ComfyUI 项目及相关第三方工具的许可协议。
- **遵守服务条款**：部署至阿里云函数计算服务，需同意阿里云服务条款和使用政策。
- **无担保声明**：本工具“按现状”提供，不包含任何形式的担保。使用风险由用户自担，开发者不负责任何直接或间接损害。
- **资源消耗**：ComfyUI 页面建立长连接请求，<span style="color:red">**持续消耗计算资源**</span>。为避免不必要费用，请不使用时关闭所有页面。

使用本工具即表示您已理解并同意以上声明。若不同意，请勿使用。

</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://images.devsapp.cn/fc-faq/33947367.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
