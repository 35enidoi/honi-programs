import express, { type Request, type Response } from 'express';
import { z, ZodError } from 'zod';

import { BrainfuckRequestSchema } from './types.js';
import { BrainFuck } from './brainfuck.js';
import { BrainFuckError } from './errors.js';


const app = express();
const port = 3000;

// とりあえず300,000ステップで制限
const maxStep = 300000;


app.use(express.json());

app.post('/execute', express.json(), (req: Request, res: Response) => {
    console.log("Received request:", req.body);
    try {
        const parsed = BrainfuckRequestSchema.parse(req.body);

        // ここでBrainfuckコードを実行するロジックを追加
        let stdout = "";
        const captureOutput = (char: string) => {
            stdout += char;
        }

        const bf = new BrainFuck({code: parsed.code, stdout_function: captureOutput});
        bf.interpret({ input: parsed.input || "", maxSteps: maxStep });

        return res.status(200).json({ output: stdout });
    } catch (error) {
        if (error instanceof ZodError) {
            console.error("Validation error:", error.issues);
            return res.status(400).json({ message: "Invalid request", error: error.issues });
        } else if (error instanceof BrainFuckError) {
            console.error("Brainfuck execution error:", error.message);
            return res.status(422).json({ message: "Brainfuck execution error", error: error.message });
        }
        console.error("Unexpected error:", error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
});


app.listen(port , () => {
    console.log(`Server is running at http://localhost:${port}`);
});
