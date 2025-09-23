export class BrainFuckError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "BrainFuckError";
    }
}

export class MemoryPointerOutOfBoundsError extends BrainFuckError {
    constructor() {
        super("Memory pointer out of bounds.");
        this.name = "MemoryPointerOutOfBoundsError";
    }
}

export class NoMatchingCloseBracketError extends BrainFuckError {
    constructor() {
        super("No matching ']' found.");
        this.name = "NoMatchingCloseBracketError";
    }
}

export class NoMatchingOpenBracketError extends BrainFuckError {
    constructor() {
        super("No matching '[' found.");
        this.name = "NoMatchingOpenBracketError";
    }
}

export class InputBufferEmptyError extends BrainFuckError {
    constructor() {
        super("Input buffer is empty.");
        this.name = "InputBufferEmptyError";
    }
}

export class MaxStepExceededError extends BrainFuckError {
    constructor() {
        super("Maximum execution steps exceeded.");
        this.name = "MaxStepExceededError";
    }
}
