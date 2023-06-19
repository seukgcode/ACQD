# ACQD: Annotation-based Complex Query Decomposition Model Enhanced by Table Pre-training for NL2SQL #

This is the official codebase of the paper

## Overview ##
The principle of Annotation-based Complex Query Decomposition (ACQD) model is shown in Figure 2. The main idea of ACQD is to alleviate the difficulty of encoding and decoding procedures in NL2SQL by decomposing a complex question into multiple simple questions, then using decoding results of simple questions to recover the result of original complex question. ACQD is consist of five modules: Intermediate Representation Completion framework (IRC), complex query decomposition, syntactic dependency modeling, grammar-based decoder and schema dependency learning. The input of ACQD is the concatenation of a NLQ and a database schema, which is separated by special token </s>. IRC that is fine-tuned by PLM with multiple tasks receives the input, and decomposes the complex query by annotation method with BIO labels based on contextual information in the input. Subsequently, syntactic dependency information in NLQ is employed to enrich contextual information of the input. Furthermore, a grammar-based decoder is utilized to make sure the predicted SQL statements in grammar are correct. Meanwhile, an auxiliary task, schema dependency learning, is used to learn fine-grained schema linking knowledge. Finally, the pre-defined intermediate representations are obtained from ACQD, and SQL statements can be inferred by mapping relations between grammar of intermediate representations and SQL statements.

# Usage
Please go to folder IRC to see details of pre-training and evaluating of IRC. 

# Statement
These codes are about IRC of ACQD. More codes about ACQD are preparing, and we will upload it as soon as we can.

# Thanks
These codes is modified by grappa. Thanks for taoyus's contribution.
