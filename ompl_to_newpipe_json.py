#!/usr/bin/env python3

import argparse
import datetime
import json
import re
import xml.etree.ElementTree as ET

YOUTUBE_CHANNEL_URL_REGEX = re.compile(r"http(s?)://www.youtube.com/channel/.*")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "in_filename", type=str, help="Path to the OMPL file to convert"
    )
    parser.add_argument(
        "-o",
        "--out-filename",
        type=str,
        help='Path to the Newpipe JSON file to be created - defaults to "newpipe_subscriptions_$DATETIME_STRING.json"',
        default=f"newpipe_subscriptions_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.json",
    )
    args = parser.parse_args()

    # This information comes from a newpipe export
    # taken from the latest version as of 2023-06-20
    out_json = {"app_version": "0.25.1", "app_version_int": 993, "subscriptions": []}

    tree = ET.parse(args.in_filename)
    for outline in tree.getroot().findall(".//outline"):
        if YOUTUBE_CHANNEL_URL_REGEX.match(outline.get("htmlUrl", "")):
            out_json["subscriptions"].append(
                {
                    "service_id": 0,
                    "url": outline.get("htmlUrl"),
                    "name": outline.get("text"),
                }
            )

    with open(args.out_filename, "w") as f:
        json.dump(out_json, f)


if __name__ == "__main__":
    main()
