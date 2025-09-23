export type BrainFuckOptions = {
    code: string,
    memorySize?: number,
    stdout_function?: (char: string) => void
}


export type BrainFuckInterpretOptions = {
    input: string,
    maxSteps?: number
}
