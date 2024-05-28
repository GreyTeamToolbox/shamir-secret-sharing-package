<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/GreyTeamToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/greyteamtoolbox/black-and-white-circle-256.png" alt="GreyTeamToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/GreyTeamToolbox/shamir-secret-sharing-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/GreyTeamToolbox/shamir-secret-sharing-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package">
        <img src="https://img.shields.io/github/created-at/GreyTeamToolbox/shamir-secret-sharing-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/GreyTeamToolbox/shamir-secret-sharing-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/GreyTeamToolbox/shamir-secret-sharing-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/GreyTeamToolbox/shamir-secret-sharing-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/shamir-secret-sharing-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

[Shamir's secret sharing (SSS)](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) is an efficient secret sharing algorithm for distributing
private information (the "secret") among a group. The secret cannot be revealed unless a quorum of the group acts together to pool their knowledge.

To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient
number of shares are combined. SSS has the property of information-theoretic security, meaning that even if an attacker steals some shares, it is
impossible for the attacker to reconstruct the secret unless they have stolen the quorum number of shares.

## Installation

```sh
pip install wolfsoftware.shamir-secret-sharing
```

## Command Line Usage

```sh
usage: shamir-secret-sharing [-h] [-V] [-s SHARES] [-t THRESHOLD] [-o] (-c CREATE | -r SHARE [SHARE ...])

Shamir's Secret Sharing CLI

flags:
  -h, --help            Show this help message and exit
  -V, --version         Show program's version number and exit.

optional:
  -s SHARES, --shares SHARES
                        Total number of shares to create (default: None)
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold number of shares needed to reconstruct the secret (default: None)
  -o, --output          Output shares to screen instead of writing to files (default: False)

required:
  -c CREATE, --create CREATE
                        The secret to share or the file containing the secret (default: None)
  -r SHARE [SHARE ...], --reconstruct SHARE [SHARE ...]
                        List of shares in the form "x,y" or file paths ending with .txt (default: None)
```

### Creating Shares

```sh
shamir-secret-sharing -c "mysupersecretpassword" -s 5 -t 3
```

### Reconstructing the Secret

```sh
shamir-secret-sharing -r share-1.txt share-3.txt share-5.txt
```

## Limitations

Secrets are limited to a max size of `4096 bytes`. If you have a secret which is larger than that, then we recommend you split it into 4K blocks
and then use this tool per block, and when you reconstruct the file parts then you can simply reconstruct the original file from there.

### Splitting Large files

```sh
split -b 4096 original_file block_
```

### Reconstructing the File from 4K Blocks

```sh
cat block_* > reconstructed_file
```

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
