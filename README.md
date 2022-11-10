# PythonでQRコードを生成してみる
***

今回使用したライブラリ[qrcode](https://pypi.org/project/qrcode/)

qrcodeを使用するにはライブラリをインストールする必要がある  
以下をコマンドラインで実行  
`pip install qrcode[pil]`

## qrcodeライブラリを軽く紹介

なんと言ってもコード3行でQRコードを生成可能！！  
`import qrcode`  
`img = qrcode.make('任意のURL')`  
`img.save("任意の画像名.png")`  
