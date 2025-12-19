# wget

`wget` utility is a command-line tool for downloading files using the HTTP protocol.

## Usage

```shell
wget [options] ... URL
```

### Options

- `h`: Displays help information.

- `O`: Specifies the output file path for the downloaded content. If not provided, the file is saved with
the name extracted from the URL in the current directory.

- `d`: Enables debug mode, providing verbose output about the download process,
including the HTTP request and response details.

### Arguments

- `URL`: The URL of the file to download
