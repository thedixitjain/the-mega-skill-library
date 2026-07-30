---
name: implementing-envelope-encryption-with-aws-kms
description: "Envelope encryption is a strategy where data is encrypted with a data encryption key (DEK), and the DEK itself is encrypted with a master key (KEK) managed by AWS KMS. This approach allows encrypting"
category: security-and-compliance
source_repo: mukul975/Anthropic-Cybersecurity-Skills
source_path: "skills/implementing-envelope-encryption-with-aws-kms/SKILL.md"
source_url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/HEAD/skills/implementing-envelope-encryption-with-aws-kms/SKILL.md
---

# Implementing Envelope Encryption with AWS KMS

## Overview

Envelope encryption is a strategy where data is encrypted with a data encryption key (DEK), and the DEK itself is encrypted with a master key (KEK) managed by AWS KMS. This approach allows encrypting large volumes of data locally while keeping the master key secure in a hardware security module (HSM) managed by AWS. This skill covers implementing envelope encryption using AWS KMS GenerateDataKey API.


## When to Use

- When deploying or configuring implementing envelope encryption with aws kms capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Familiarity with cryptography concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Objectives

- Understand the envelope encryption pattern and its advantages
- Generate data encryption keys using AWS KMS GenerateDataKey
- Encrypt/decrypt data locally using DEKs
- Store encrypted DEK alongside ciphertext
- Implement key caching to reduce KMS API calls
- Handle key rotation with automatic re-encryption
- Implement multi-region encryption for disaster recovery

## Key Concepts

### Envelope Encryption Flow

1. Call `kms:GenerateDataKey` to get plaintext DEK + encrypted DEK
2. Use plaintext DEK to encrypt data locally (AES-256-GCM)
3. Store encrypted DEK alongside ciphertext
4. Discard plaintext DEK from memory
5. For decryption: call `kms:Decrypt` on encrypted DEK, then decrypt data

### Advantages Over Direct KMS Encryption

| Aspect | Direct KMS | Envelope Encryption |
|--------|-----------|-------------------|
| Max data size | 4 KB | Unlimited |
| Latency | Network round-trip per operation | Local encryption |
| Cost | $0.03/10,000 requests | Fewer KMS requests |
| Offline | Not possible | Yes (with cached DEKs) |

### KMS Key Types

- **AWS Managed**: AWS creates and manages (`aws/s3`, `aws/ebs`)
- **Customer Managed**: You create and manage policies
- **Custom Key Store**: Backed by CloudHSM cluster

## Security Considerations

- Never store plaintext DEK; only keep encrypted DEK
- Use key policies to restrict who can call GenerateDataKey and Decrypt
- Enable AWS CloudTrail logging for all KMS API calls
- Implement key rotation (automatic annual rotation for CMKs)
- Use encryption context for authenticated encryption metadata
- Handle KMS throttling with exponential backoff

## Validation Criteria

- [ ] GenerateDataKey returns plaintext and encrypted DEK
- [ ] Data encrypts correctly with plaintext DEK using AES-256-GCM
- [ ] Encrypted DEK can be decrypted via KMS Decrypt API
- [ ] Decrypted DEK recovers the original data
- [ ] Plaintext DEK is wiped from memory after use
- [ ] Encryption context is validated during decryption
- [ ] Key rotation re-encrypts DEKs with new master key

---

**Source:** [`mukul975/Anthropic-Cybersecurity-Skills`](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) → `skills/implementing-envelope-encryption-with-aws-kms/SKILL.md`
