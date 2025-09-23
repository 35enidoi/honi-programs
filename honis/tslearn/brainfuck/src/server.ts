import express, { type Request, type Response } from 'express';
import { z, ZodError } from 'zod';

import { BrainfuckRequestSchema } from './enum.js';
import { BrainFuck } from './brainfuck.js';
import { BrainFuckError } from './errors.js';


const app = express();
const port = 3000;


app.use(express.json());

app.post('/execute', express.json(), (req: Request, res: Response) => {
    console.log("Received request:", req.body);
    try {
        const parsed = BrainfuckRequestSchema.parse(req.body);

        // ここでBrainfuckコードを実行するロジックを追加
        const bf = new BrainFuck(parsed.code);
        bf.interpret(parsed.input || "");
        return res.status(200).json({ test: "ok"});
    } catch (error) {
        if (error instanceof ZodError) {
            console.error("Validation error:", error.issues);
            return res.status(400).json({message: "Invalid request", error: error.issues});
        } else if (error instanceof BrainFuckError) {
            console.error("Brainfuck execution error:", error.message);
            return res.status(400).json({message: "Brainfuck execution error", error: error.message});
        }
        console.error("Unexpected error:", error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
});


app.listen(port , () => {
    console.log(`Server is running at http://localhost:${port}`);
});
