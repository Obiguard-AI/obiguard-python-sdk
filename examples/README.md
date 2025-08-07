# Obiguard AI examples

The examples in this repository demonstrate how to use the Obiguard Python SDK to enhance the security and performance
of your AI applications. Each example is designed to showcase how you may observe and control the behavior of your AI
application from [Obiguard logs](https://docs.obiguard.ai/observability/logs).

## Getting your virtual key

Obiguard’s virtual key system lets you securely store your LLM API keys in our vault and manage them easily using a
unique virtual identifier.

Read more about virtual keys in the [Obiguard virtual keys documentation](https://docs.obiguard.ai/virtual-keys).

## Usage

The examples in this repository use the Obiguard virtual key, which is a unique key to identify your LLM provider's API
key onboarded in Obiguard.

You may also set your Obiguard virtual key in the `OBIGUARD_VIRTUAL_KEY` environment variable, which will be used by the
SDK. This allows you to omit the use of `obiguard_virtual_key` in the code examples.

The `Qwen/Qwen2.5-32B-Instruct` model was used in the examples, but you can replace it with any model supported by your
AI provider (OpenAI, Anthropic, etc.) by changing the model name in the code.

Examples on the use of [OpenAI's Response AI](https://platform.openai.com/docs/api-reference/responses) requires an
OpenAI API key, which can be set in the `OPENAI_API_KEY` environment variable. Additionally, the Obiguard API key is
required and can be obtained from
the [Policy Group](https://docs.obiguard.ai/guardrail-AI/guardrail-validators#3-generate-an-api-key-for-the-policy-group)
page.

## Documentation page

https://docs.obiguard.ai