# Offline_GPT: Secure, Local Conversations with Your Documents 🌐

**Offline_GPT** is an open-source initiative that allows you to converse with your documents without compromising your privacy. With everything running locally, you can be assured that no data ever leaves your computer. Dive into the world of secure, local document interactions with LocalGPT.

## Features 🌟
- **Utmost Privacy**: Your data remains on your computer, ensuring 100% security.
- **Versatile Model Support**: Seamlessly integrate a variety of open-source models, including HF, GPTQ, GGML, and GGUF.
- **Diverse Embeddings**: Choose from a range of open-source embeddings.
- **Reuse Your LLM**: Once downloaded, reuse your LLM without the need for repeated downloads.
- **Chat History**: Remembers your previous conversations (in a session).
- **API**: LocalGPT has an API that you can use for building RAG Applications.
- **Graphical Interface**: LocalGPT comes with two GUIs, one uses the API and the other is standalone (based on streamlit).
- **GPU, CPU & MPS Support**: Supports multiple platforms out of the box, Chat with your data using `CUDA`, `CPU` or `MPS` and more!
- 
## Technical Details 🛠️
By selecting the right local models and the power of `LangChain` you can run the entire RAG pipeline locally, without any data leaving your environment, and with reasonable performance.

- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `InstructorEmbeddings`. It then stores the result in a local vector database using `Chroma` vector store.
- `run_localGPT.py` uses a local LLM to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- You can replace this local LLM with any other LLM from the HuggingFace. Make sure whatever LLM you select is in the HF format.

This project was inspired by the original [privateGPT]([https://github.com/PromtEngineer/localGPT]).

## Built Using 🧩
- [LangChain](https://github.com/hwchase17/langchain)
- [HuggingFace LLMs](https://huggingface.co/models)
- [InstructorEmbeddings](https://instructor-embedding.github.io/)
- [LLAMACPP](https://github.com/abetlen/llama-cpp-python)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)

# Environment Setup 🌍

1. 📥 Clone the repo using git:

```shell
git clone https://github.com/kishan-rajoria/PowergenAI/tree/main/Offline_GPT.git
```

2. 🐍 Install [conda](https://www.anaconda.com/download) for virtual environment management. Create and activate a new virtual environment.

```shell
conda create -n localGPT python=3.10.0
conda activate localGPT
```

3. 🛠️ Install the dependencies using pip

To set up your environment to run the code, first install all requirements:

```shell
pip install -r requirements.txt
```

***Installing LLAMA-CPP :***

LocalGPT uses [LlamaCpp-Python](https://github.com/abetlen/llama-cpp-python) for GGML (you will need llama-cpp-python <=0.1.76) and GGUF (llama-cpp-python >=0.1.83) models.


If you want to use BLAS or Metal with [llama-cpp](https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast--metal) you can set appropriate flags:

For `NVIDIA` GPUs support, use `cuBLAS`

```shell
# Example: cuBLAS
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
```

For Apple Metal (`M1/M2`) support, use

```shell
# Example: METAL
CMAKE_ARGS="-DLLAMA_METAL=on"  FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
```
For more details, please refer to [llama-cpp](https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast--metal)

## Docker 🐳

Installing the required packages for GPU inference on NVIDIA GPUs, like gcc 11 and CUDA 11, may cause conflicts with other packages in your system.
As an alternative to Conda, you can use Docker with the provided Dockerfile.
It includes CUDA, your system just needs Docker, BuildKit, your NVIDIA GPU driver and the NVIDIA container toolkit.
Build as `docker build . -t localgpt`, requires BuildKit.
Docker BuildKit does not support GPU during *docker build* time right now, only during *docker run*.
Run as `docker run -it --mount src="$HOME/.cache",target=/root/.cache,type=bind --gpus=all localgpt`.

## Test dataset

For testing, this repository comes with [Constitution of USA](https://constitutioncenter.org/media/files/constitution.pdf) as an example file to use.

## Ingesting your OWN Data.
Put you files in the `SOURCE_DOCUMENTS` folder. You can put multiple folders within the `SOURCE_DOCUMENTS` folder and the code will recursively read your files.

### Support file formats:
LocalGPT currently supports the following file formats. LocalGPT uses `LangChain` for loading these file formats. The code in `constants.py` uses a `DOCUMENT_MAP` dictionary to map a file format to the corresponding loader. In order to add support for another file format, simply add this dictionary with the file format and the corresponding loader from [LangChain](https://python.langchain.com/docs/modules/data_connection/document_loaders/).

```shell
DOCUMENT_MAP = {
    ".txt": TextLoader,
    ".md": TextLoader,
    ".py": TextLoader,
    ".pdf": PDFMinerLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".docx": Docx2txtLoader,
    ".doc": Docx2txtLoader,
}
```

### Ingest

Run the following command to ingest all the data.

If you have `cuda` setup on your system.

```shell
python ingest.py
```
You will see an output like this:
<img width="1110" alt="Screenshot 2023-09-14 at 3 36 27 PM" src="https://github.com/PromtEngineer/localGPT/assets/134474669/c9274e9a-842c-49b9-8d95-606c3d80011f">


Use the device type argument to specify a given device.
To run on `cpu`

```sh
python ingest.py --device_type cpu
```

To run on `M1/M2`

```sh
python ingest.py --device_type mps
```

Use help for a full list of supported devices.

```sh
python ingest.py --help
```

This will create a new folder called `DB` and use it for the newly created vector store. You can ingest as many documents as you want, and all will be accumulated in the local embeddings database.
If you want to start from an empty database, delete the `DB` and reingest your documents.

Note: When you run this for the first time, it will need internet access to download the embedding model (default: `Instructor Embedding`). In the subsequent runs, no data will leave your local environment and you can ingest data without internet connection.

## Ask questions to your documents, locally!

In order to chat with your documents, run the following command (by default, it will run on `cuda`).

```shell
python run_localGPT.py
```
You can also specify the device type just like `ingest.py`

```shell
python run_localGPT.py --device_type mps # to run on Apple silicon
```

This will load the ingested vector store and embedding model. You will be presented with a prompt:

```shell
> Enter a query:
```

After typing your question, hit enter. LocalGPT will take some time based on your hardware. You will get a response like this below.
<img width="1312" alt="Screenshot 2023-09-14 at 3 33 19 PM" src="https://github.com/PromtEngineer/localGPT/assets/134474669/a7268de9-ade0-420b-a00b-ed12207dbe41">

Once the answer is generated, you can then ask another question without re-running the script, just wait for the prompt again.


***Note:*** When you run this for the first time, it will need internet connection to download the LLM (default: `TheBloke/Llama-2-7b-Chat-GGUF`). After that you can turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

Type `exit` to finish the script.

### Extra Options with run_localGPT.py

You can use the `--show_sources` flag with `run_localGPT.py` to show which chunks were retrieved by the embedding model. By default, it will show 4 different sources/chunks. You can change the number of sources/chunks

```shell
python run_localGPT.py --show_sources
```

Another option is to enable chat history. ***Note***: This is disabled by default and can be enabled by using the  `--use_history` flag. The context window is limited so keep in mind enabling history will use it and might overflow.

```shell
python run_localGPT.py --use_history
```


# Run the Graphical User Interface

1. Open `constants.py` in an editor of your choice and depending on choice add the LLM you want to use. By default, the following model will be used:

   ```shell
   MODEL_ID = "TheBloke/Llama-2-7b-Chat-GGUF"
   MODEL_BASENAME = "llama-2-7b-chat.Q4_K_M.gguf"
   ```

3. Open up a terminal and activate your python environment that contains the dependencies installed from requirements.txt.

4. Navigate to the `/LOCALGPT` directory.

5. Run the following command `python run_localGPT_API.py`. The API should being to run.

6. Wait until everything has loaded in. You should see something like `INFO:werkzeug:Press CTRL+C to quit`.

7. Open up a second terminal and activate the same python environment.

8. Navigate to the `/LOCALGPT/localGPTUI` directory.

9. Run the command `python localGPTUI.py`.

10. Open up a web browser and go the address `http://localhost:5111/`.


# How to select different LLM models?

To change the models you will need to set both `MODEL_ID` and `MODEL_BASENAME`.

1. Open up `constants.py` in the editor of your choice.
2. Change the `MODEL_ID` and `MODEL_BASENAME`. If you are using a quantized model (`GGML`, `GPTQ`, `GGUF`), you will need to provide `MODEL_BASENAME`. For unquantized models, set `MODEL_BASENAME` to `NONE`
5. There are a number of example models from HuggingFace that have already been tested to be run with the original trained model (ending with HF or have a .bin in its "Files and versions"), and quantized models (ending with GPTQ or have a .no-act-order or .safetensors in its "Files and versions").
6. For models that end with HF or have a .bin inside its "Files and versions" on its HuggingFace page.

   - Make sure you have a `MODEL_ID` selected. For example -> `MODEL_ID = "TheBloke/guanaco-7B-HF"`
   - Go to the [HuggingFace Repo](https://huggingface.co/TheBloke/guanaco-7B-HF)

7. For models that contain GPTQ in its name and or have a .no-act-order or .safetensors extension inside its "Files and versions on its HuggingFace page.

   - Make sure you have a `MODEL_ID` selected. For example -> model_id = `"TheBloke/wizardLM-7B-GPTQ"`
   - Got to the corresponding [HuggingFace Repo](https://huggingface.co/TheBloke/wizardLM-7B-GPTQ) and select "Files and versions".
   - Pick one of the model names and set it as  `MODEL_BASENAME`. For example -> `MODEL_BASENAME = "wizardLM-7B-GPTQ-4bit.compat.no-act-order.safetensors"`

8. Follow the same steps for `GGUF` and `GGML` models.
