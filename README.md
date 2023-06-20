# OMPL to Newpipe JSON

A simple script to convert all youtube channel URLs from an OMPL file to Newpipe's JSON format for subscriptions. The OMPL may contain non-youtube entries. Only matching channel URLs will be included in the file created for Newpipe.

## Requirements
python3

## Usage
`python3 $PATH_TO_OMPL_FILE`

## Arguments
|Short Name|Long Name|Type|Description|
|-|-|-|-|
||`in_filename`|`str`|Path to the OMPL file to convert|
|`-o`|`--out-filename`|`str`|Path to the Newpipe JSON file to be created - defaults to "newpipe\_subscriptions_$DATETIME\_STRING.json"|

