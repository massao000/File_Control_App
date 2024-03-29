<p align="center">
  <h1 align="center">File Control App</h2>
</p>
<p align="center">
  <a href="https://img.shields.io/badge/Python-v3.9.0-blue">
    <img src="https://img.shields.io/badge/Python-v3.9.0-blue"alt="python">
  </a>
  <a href="https://img.shields.io/badge/PySimpleGUI-4.39.1-blue">
    <img src="https://img.shields.io/badge/PySimpleGUI-4.39.1-blue"alt="PySimpleGUI">
  </a>
  <a href="https://img.shields.io/badge/-Windows-blue">
    <img src="https://img.shields.io/badge/-Windows-blue"alt="PySimpleGUI">
  </a>

[sequence_numberのGUI番](https://github.com/massao000/sequence_number)

# アプリケーション概要

## 簡単にこれらのことができるGUIアプリケーション
* 連番ファイル作成
* ファイル名変更
* 連番付与
* テンプレート

## カスタマイズ機能
* `template` フォルダ
    * 自分だけのフォルダorファイルのテンプレートが作成可能

* `customize_ex.txt`
    * 使う拡張子だけのカスタマイズ



# 機能

## 連番ファイル作成

フォルダに新規ファイルを連番で生成が可能

<a href="img" ><img src="https://user-images.githubusercontent.com/69783019/121014295-c8c0ba00-c7d4-11eb-9b82-f810e7b05e83.png" width="500" alt="Sequence Number"></a>

* 保存場所
    * 検索ボタンを押すと、エクスプローラーが開きフォルダだけが選択できます
* ファイル名
    * 連番ファイルのファイル名
* 拡張子入力または選択
    * 拡張子の選択
* ファイル数
    * 連番ファイルの作成数
* ファイルタイプ
    * ON/OFF　チェックボタンを押すと、連番タイプが0詰めか、0詰めなしか変更できる
    * 連番ファイルのタイプ選択
* 更新ボタン
    * 想定されるファイル名のチェックができる
* 実行ボタン
    * 作成の開始ボタン

<br>

## ファイル名変更

ファイルを同じ名前で連番ファイルにすることが可能

拡張子を一括で変更が可能

<a href="img" ><img src="https://user-images.githubusercontent.com/69783019/121014311-cc544100-c7d4-11eb-8f4a-226c00d63820.png" width="500" alt="File Rename"></a>

* 単一ファイルに変更or複数変更ボタン
    * 単一ファイルと複数変更の検索ボタンの切り替え
* 拡張子変更
    * 拡張子だけ変えるオプション
    * チェックが入るとファイル名とファイルタイプの変更を無効にします
* 単一ファイル
    * 検索ボタンを押すと、エクスプローラーが開きファイルだけが選択できます
    * 既存ファイルのファイル名変更
    * 単一のファイルの選択
* 複数変更
    * 検索ボタンを押すと、エクスプローラーが開きファイルだけが選択できます
    * 複数のファイルでの変更が可能
    * バラバラのファイルを同じ名前で連番ファイルに変更が可能
    * 一括で拡張子の変更が可能
* ファイル名
    * 連番ファイルのファイル名
* 拡張子入力または選択
    * 拡張子の選択
* ファイルタイプ
    * ON/OFF　チェックボタンを押すと、連番タイプが0詰めか、0詰めなしか変更できる
    * 連番ファイルのタイプ選択
* 実行ボタン
    * 作成の開始ボタン

<br>

## 連番付与

既存のファイル名前に変更を加えずに連番をつけることが可能

<a href="img" ><img src="https://user-images.githubusercontent.com/69783019/121014325-d0805e80-c7d4-11eb-9baa-eeb1d07a6642.png" width="500" alt="Grant"></a>

* 付与ファイル
    * 複数ファイルの選択が可能
    * 検索ボタンを押すと、エクスプローラーが開きフォルダだけが選択できます
* ファイルタイプ
    * ON/OFF　チェックボタンを押すと、連番タイプが0詰めか、0詰めなしか変更できる
    * 連番ファイルのタイプ選択
* 実行ボタン
    * 作成の開始ボタン


<br>

## テンプレート

`templates`フォルダにテンプレートのファルダまたは、ファイルの複製が可能

<a href="img" ><img src="https://user-images.githubusercontent.com/69783019/121014342-d5451280-c7d4-11eb-9523-550862fe332f.png" width="500" alt="Templates"></a>

* 保存場所
    * 検索ボタンを押すと、エクスプローラーが開きフォルダだけが選択できます
* 保存名
    * フォルダの名前を決める
* テンプレート
    * `templates`フォルダに保存してあるフォルダまたは、ファイルの選択
* 実行ボタン
    * 作成の開始ボタン


## デモ
[YouTube](https://youtu.be/pn3fznacraQ)

<div>
    <h1 align="center">連番作成</h1>
    <img src="https://user-images.githubusercontent.com/69783019/121341103-4dd5db80-c95b-11eb-9735-e81003ecf0a1.gif" width="500" alt="demo1">
</div>

<br>

<div>
    <h1 align="center">ファイル名変更</h1>
    <img src="https://user-images.githubusercontent.com/69783019/121675388-4bf05180-caee-11eb-9258-901cadbe73e8.gif" width="500" alt="demo2">
</div>

<br>

<div>
<h1 align="center">連番付与</h1>
    <img src="https://user-images.githubusercontent.com/69783019/121341270-752ca880-c95b-11eb-836a-92f2e69fadcd.gif" width="500" alt="demo3">
</div>

<br>

<div>
<h1 align="center">テンプレート</h1>
    <img src="https://user-images.githubusercontent.com/69783019/121341281-778f0280-c95b-11eb-844b-0e616dea3a93.gif" width="500" alt="demo4">
</div>

# 設計

* `File_Control_App.exe`
    * アプリケーションファイル
* `main.py`
    * メインプログラムファイル
* package
    * `main.py`のプログラムパッケージフォルダ
* template フォルダ
    * 自分のテンプレートファイルorフォルダを保存できる
* `customize_ex.txt`
    * 拡張子のカスタマイズが可能


## モジュール

<br>
pythonGUIモジュール

```pip install
$ pip install PySimpleGUI
```
<br>
python標準ファイル操作モジュール

```pip install
$ pip install os
```
<br>
python標準ファイル操作モジュール

```pip install
$ pip install shutil
```
<br>
python標準ファイル操作モジュール

```pip install
$ pip install glob
```

* PySimpleGUI
* os
* shutil
* glob

## 備考
