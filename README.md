# AudioClient
 一个语音客户端，使用Python及Pyside6



## 基础配置

查阅：[CONTRIBUTING](CONTRIBUTING.md)



## 生产环境

如果您想为APOC模拟飞行平台贡献代码，请注意以下细节：

在 `config.yaml` 中，替换为以下内容：

```yaml
account: # 账户
  password: '' # 密码
  remember_me: false # 是否记住我
  username: '' # 三元组
audio:
  api_driver: "\u81EA\u52A8" # Windows 音频 API 驱动器
  input_device: "\u9EA6\u514B\u98CE (HECATE G1 PRO GAMING HEADSET)" # 设备（默认）
  output_device: "\u626C\u58F0\u5668 (HECATE G1 PRO GAMING HEADSET)" # 设备（默认）
  ptt_key: Key.ctrl_r # Push To Talk 按键
log: # 日志
  compression: zip # 压缩包格式
  level: TRACE # 日志登记
  path: logs/{time}.log # 日志路径及名称
  retention: 7 days # 日志保存时间
  rotation: 1 day # 日志轮转
server:
  api_endpoint: https://api.apocfly.com # api端点
  voice_endpoint: voice.apocfly.com # 语音端点
  voice_tcp_port: 6808 # 语音TCP端口
  voice_udp_port: 6807 # 语音UDP端口
version: 1.0.0 # 版本

```



