import { z } from 'zod';


export const BrainfuckRequestSchema = z.object({
    code: z.string().min(1, "Code cannot be empty"),
    input: z.string().optional()
});


export type BrainFuckOptions = {
    code: string,
    memorySize?: number,
    stdout_function?: (char: string) => void
}


export type BrainFuckInterpretOptions = {
    input: string,
    maxSteps?: number
}
