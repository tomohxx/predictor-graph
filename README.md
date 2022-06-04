# Predictor Graph

聴牌している他家がある牌を待つ確率を以下の式で計算しグラフで出力する. なお, 使用するアルゴリズムは動的計画法である(モンテカルロ法ではない).

$$
(\text{ある牌を待つ確率}) = \frac{(\text{その牌を待つ聴牌形の数})}{(\text{すべての聴牌形の数})}
$$

## 使用方法

1. このリポジトリをクローンする.

    ```
    $ git clone --recursive https://github.com/tomohxx/predictor-graph.git
    $ cd predictor-graph
    ```

1. [wall_river.txt](wall_river.txt)に他家の手牌の面子数と各牌の残り枚数, 振聴かどうかのフラグを入力する.

    - 1行目に手牌の面子数を入力する(4は門前を意味する).
    - 2行目以降に各牌の残り枚数と振聴かどうかのフラグを入力する. 例えば1mの残り枚数が3枚, 1mが捨てられている(あるいは立直後に通っている)場合は`1m`の行に`1m 3 1`と入力する. また, 2mが自分から1枚も見えなければ`2m`の行に`2m 4 0`と入力する. 同様にして他のすべての牌について残り枚数と振聴かどうかのフラグを入力する.
    
    ```
    4
    1m 3 1
    2m 4 0
    ```

1. 以下のコマンドを実行する. [example.png](example.png)のようなグラフが`output`に出力される.

    ```
    $ docker build . -t predictor
    $ docker run -v $PWD/output:/output -v $PWD/wall_river.txt:/wall_river.txt --rm predictor
    ```

## 参考

[tomohxx/predictor](https://github.com/tomohxx/predictor)
