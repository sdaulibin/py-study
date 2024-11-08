import random
styles = [
    {"style":"现代都市","scene":"鳞次栉比的玻璃幕墙大厦，反射着阳光，在城市天际线中错落有致，马路上川流不息的汽车、快速行驶的地铁、空中的轻轨或高架桥，形成复杂的交通网络"},
    {"style":"自然风光","scene":"静谧的山谷中，有潺潺流淌的小溪，溪边生长着各种野花野草，两侧的山壁陡峭，岩石上有着岁月留下的痕迹，偶尔有飞鸟掠过"},
    {"style":"田园牧歌","scene":"大片成熟的麦子在微风中轻轻摇曳，如金色的海洋泛起波浪，麦芒在阳光下闪烁，散发出丰收的气息"}
]

def main():
    value = random.choice(styles)
    return value.get("style"),value.get("scene")

print(main())