import { readFile } from "node:fs/promises";

import { BrainFuckError } from "./errors.js";
import { BrainFuck } from "./brainfuck.js";


// BrainFuck インタプリタのCLIエントリ
// 使い方:
// 	- ファイルから実行:  node dist/main.js --file path/to/code.bf
// 	- 文字列から実行:    node dist/main.js --code "+[.+]"
// 	- 標準入力から:      echo ">+. +" | node dist/main.js

function printUsage(): void {
	// 使い方を標準エラー出力に表示
    const message =
`Usage:
    node dist/main.js [--file path | --code "brainfuck code"]
    echo '+[.+]' | node dist/main.js

Options:
  -f, --file <path>     ファイルからコードを読み込み
  -c, --code <code>     文字列のコードを使用
  -i, --input <string>  ',' の入力として使用するバッファ
  -h, --help            ヘルプを表示して終了

備考:
  --file/--code が無い場合は標準入力(パイプ)からコードを読み込みます。`;
	console.error(message);
}

// 標準入力から文字列を非同期で読み込む
async function readStdin(): Promise<string> {
	// 端末(TTY)からの実行でパイプ入力が無い場合は空文字を返す
	if (process.stdin.isTTY) return "";
	const chunks: Uint8Array[] = [];
	// NodeのstdinはAsyncIterableなので for await で読み出す
	for await (const chunk of process.stdin) {
		chunks.push(typeof chunk === "string" ? Buffer.from(chunk) : chunk);
	}
	// バッファを結合してUTF-8文字列に変換して返す
	return Buffer.concat(chunks as Buffer[]).toString("utf8");
}

// メイン処理: 引数解析 -> 入力取得 -> 実行
async function main() {
	const args = process.argv.slice(2);
    let code = ""; // 実行対象のBrainFuckコード
    let input = ""; // BrainFuckプログラムへの入力

	// 簡易引数パーサ
	for (let i = 0; i < args.length; i++) {
		const a = args[i];
		switch (a) {
			case "--file":
			case "-f": {
				// 次の引数をファイルパスとして読み込み
				const filePath = args[i + 1];
				if (filePath === undefined) {
					printUsage();
					process.exit(1);
					return;
				}
				code = await readFile(filePath, "utf8");
				i++; // 値を一つ消費
				break;
			}
			case "--code":
			case "-c": {
				// 次の引数をコード文字列として採用
				const inline = args[i + 1];
				if (inline === undefined) {
					printUsage();
					process.exit(1);
					return;
				}
				code = inline;
				i++; // 値を一つ消費
				break;
            }
            case "--help":
            case "-h":
                printUsage();
                process.exit(0);
                return;
                break;
            case "--input":
            case "-i":
                // 次の引数を入力バッファとして採用
                const inputStr = args[i + 1];
                if (inputStr === undefined) {
                    printUsage();
                    process.exit(1);
                    return;
                }
                input = inputStr;
                i++; // 値を一つ消費
                break;
			default:
				// 未知のフラグは無視
				break;
		}
	}

	// 引数で未指定なら標準入力から取得
	if (!code) {
		code = await readStdin();
	}

	// それでも空なら使い方を表示して終了
	if (!code) {
		printUsage();
		process.exit(1);
		return;
    }

	// インタプリタを実行
	const bf = new BrainFuck(code);
	bf.interpret(input);
}

// 例外はここで拾って非ゼロ終了
main().catch((err) => {
	if (err instanceof BrainFuckError) {
		console.error(`BrainFuckError: ${err.message}`);
	} else {
		console.error(`Unknown error: ${err}`);
	}
	process.exit(1);
});
