FROM ollama/ollama

# Pull model that will be used for RAG
RUN ollama serve & sleep 5 && ollama pull llama3

ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]