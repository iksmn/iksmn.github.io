---
layout: post
title:  "Flutter e Linux Mint"
date: 14-02-2026
categories: [documentation, linux]
tag: [linux, mint, flutter, mobile]
---
# Flutter e Linux Mint

Na matéria de Desenvolvimento Mobile é utilizado o framework Flutter mas como esperado as aulas utilizam Windows. Como decidi utilizar Linux (nesse momento o Mint) para aprender mais sobre o sistema também tive a necessidade de buscar formas de instalar o Flutter no sistema. Assim segui os passos abaixo:

## Download e Instalação

Conforme solicitado pela documentação verifiquei se os pacotes estavam disponíveis nos sistema:

<li>
    <code>curl</code>
</li>
<li>
    <code>git</code>
</li><li>
    <code>unzip</code>
</li><li>
    <code>xz-utils</code>
</li><li>
    <code>zip</code>
</li>
<li>
    <code>libglu1-mesa</code>
</li>    
<br>
Para instalar os pacotes usei o comando:

```
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa
```
Como o Mint é baseado no Ubuntu o comando <code>apt-get</code> é utilizado. <br>
Os passos seguintes foram baixar o SDK FLutter do site do próprio framework que para Linux está compactado na extensão .tar.xz.  
É indicado a criação de um diretório chamado <code>~/develop/</code> e a extração do SDK nessa pasta.  

## Adicionando Flutter ao PATH (Caminho do Sistema)

Feito isso é necessário adicionar o Flutter ao caminho do sistema, que é o local que entendo como sendo o endereço onde as váriáveis globais do sistema operacional vão encontrar a aplicação para que seja possível executar a mesma via Terminal. Sei que isso é feito para Java também.

Nesse ponto é necessário descobrir qual Shell estou usando (O que é Shell e suas váriações é um tema que deverá ser estudado e publicado também).

Para descobrir o Shell utilizei:
```
$ echo $SHELL
```
O resultado foi esse:
```
/bin/bash
```

O comando utilizado para adicionar o PATH utilizando Bash é:

```
echo 'export PATH="$HOME/develop/flutter/bin:$PATH"' >> ~/.bashrc
```
Após isso executei os comandos para verificar se a instalação no sistema e o PATH estavam correntos:

```
flutter --version
dart --version
```
Sendo o resultado:

```
Flutter 3.38.9 • channel stable • https://github.com/flutter/flutter.git
Framework • revision 67323de285 (3 weeks ago) • 2026-01-28 13:43:12 -0800
Engine • hash 5eb06b7ad5bb8cbc22c5230264c7a00ceac7674b (revision 587c18f873) (19
days ago) • 2026-01-27 23:23:03.000Z
Tools • Dart 3.10.8 • DevTools 2.51.1
Dart SDK version: 3.10.8 (stable) (Tue Jan 27 00:02:04 2026 -0800) on "linux_x64"
```
Com isso a instalação do Flutter e a adição ao PATH está finalizada.

## Referências

https://docs.flutter.dev/install/manual

{% include embed/youtube.html id='M5pRZBbOReo' %}