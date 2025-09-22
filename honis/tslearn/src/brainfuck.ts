import {
    InputBufferEmptyError, NoMatchingCloseBracketError,
    NoMatchingOpenBracketError, MemoryPointerOutOfBoundsError
} from "./errors.js";


export class BrainFuck {
    private inputBuffer: string = "";
    private code: string;
    private memory: number[];
    private memoryPointer: number = 0;
    private codePointer: number = 0;
    private loopStack: number[] = [];

    constructor(code: string, memorySize: number = 30000) {
        this.code = code;
        this.memory = new Array(memorySize).fill(0);
    }

    private cursorPosIncrement(): void {
        if (this.memoryPointer >= this.memory.length - 1) {
            throw new MemoryPointerOutOfBoundsError();
        }
        this.memoryPointer++;
    }

    private cursorPosDecrement(): void {
        if (this.memoryPointer <= 0) {
            throw new MemoryPointerOutOfBoundsError();
        }
        this.memoryPointer--;
    }

    private memoryIncrement(): void {
        if (this.memory[this.memoryPointer]! >= 255) {
            this.memory[this.memoryPointer] = 0; // オーバーフロー時に0に戻す
            return;
        }
        this.memory[this.memoryPointer]!++;
    }

    private memoryDecrement(): void {
        if (this.memory[this.memoryPointer]! <= 0) {
            this.memory[this.memoryPointer] = 255; // アンダーフロー時に255に戻す
            return;
        }
        this.memory[this.memoryPointer]!--;
    }

    private loopStart(): void {
        if (this.memory[this.memoryPointer] === 0) {
            let openBrackets = 1;
            while (openBrackets > 0) {
                this.codePointer++;

                if (this.codePointer >= this.code.length) {
                    throw new NoMatchingCloseBracketError();
                }

                switch (this.code[this.codePointer]) {
                    case "[":
                        openBrackets++;
                        break;
                    case "]":
                        openBrackets--;
                        break;
                }
            }
        } else {
            // '[' の位置を積む（codePointer は '[' を指している）
            this.loopStack.push(this.codePointer);
        }
    }

    private loopEnd(): void {
        // ']' に対応する '[' がスタックに無い場合は不正
        if (this.loopStack.length === 0) {
            throw new NoMatchingOpenBracketError();
        }

        if (this.memory[this.memoryPointer] !== 0) {
            // ループ継続: 対応する '[' に戻す（外側で codePointer++ されて直後の命令に進む）
            this.codePointer = this.loopStack.at(-1)!;
        } else {
            // ループ終了: '[' を取り出す
            this.loopStack.pop();
        }
    }

    private output(): void {
        const char = String.fromCharCode(this.memory[this.memoryPointer]!);
        process.stdout.write(char);
    }

    private input(): void {
        if (this.inputBuffer.length > 0) {
            this.memory[this.memoryPointer] = this.inputBuffer.charCodeAt(0);
            this.inputBuffer = this.inputBuffer.slice(1);
        } else {
            // TODO 例外用クラスの作成
            throw new InputBufferEmptyError();
        }
    }

    public interpret(input: string): void {
        this.inputBuffer = input;
    
        while (this.codePointer < this.code.length) {
            switch (this.code[this.codePointer]) {
                case ">":
                    this.cursorPosIncrement();
                    break;
                case "<":
                    this.cursorPosDecrement();
                    break;
                case "+":
                    this.memoryIncrement();
                    break;
                case "-":
                    this.memoryDecrement();
                    break;
                case "[":
                    this.loopStart();
                    break;
                case "]":
                    this.loopEnd();
                    break;
                case ".":
                    this.output();
                    break;
                case ",":
                    this.input();
                    break;
            }
            this.codePointer++;
        }
    }
}
