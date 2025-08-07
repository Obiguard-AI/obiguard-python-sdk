# Obiguard AI examples

The examples in this repository demonstrate how to use the Obiguard Python SDK to enhance the security and performance
of your AI applications. Each example is designed to showcase different features and functionalities of the Obiguard
platform.

## Getting your virtual key

Obiguard’s virtual key system lets you securely store your LLM API keys in our vault and manage them easily using a
unique virtual identifier.

Read more about virtual keys in the [Obiguard virtual keys documentation](https://docs.obiguard.ai/virtual-keys).

## Usage

The examples in this repository use the `obiguard` virtual key, which is a placeholder for your actual AI provider's API
key.

You may also set your Obiguard virtual key in the `OBIGUARD_VIRTUAL_KEY` environment variable, which will be used by the
SDK. This allows you to omit the use of `obiguard_virtual_key` in the code examples.

The `Qwen/Qwen2.5-32B-Instruct` model was used in the examples, but you can replace it with any model supported by your
AI provider (OpenAI, Anthropic, etc.) by changing the model name in the code.

## Documentation page

https://docs.obiguard.ai