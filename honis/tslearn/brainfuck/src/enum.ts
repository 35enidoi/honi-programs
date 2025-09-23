import { z } from 'zod';


export const BrainfuckRequestSchema = z.object({
    code: z.string().min(1, "Code cannot be empty"),
    input: z.string().optional()
});
