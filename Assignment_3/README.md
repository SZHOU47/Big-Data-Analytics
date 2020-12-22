# Assignment - Spark RDD and SparkSQL

**You should thoroughly read through the entire assignment before beginning your work! Don't start the cluster until you are ready.**

## Start your cluster

Start EMR Cluster with cluster configuration and bootstrap actions as described in the [reference for starting a cluster using bootstrap actions and software customization for Spark.](https://github.com/bigdatateaching/using-bootstrap-actions)

**Recommended setup:** 1 master and 4 core of m5.xlarge

## Connect to the cluster

* Once the cluster is in "Waiting" mode (should only take a few minutes), ssh into the master **with local port forwarding (-L)**, and with **agent forwarding (-A) if necessary**:

```
ssh-add
ssh -A -L 8765:localhost:8765 hadoop@...
```
* Run your `git-config` commands
* Clone your repository to the master node


### Provide the Master Node and Cluster Metadata

Provide the instance metadata. Run this command in the master node command line.

```
curl http://169.254.169.254/latest/dynamic/instance-identity/document/ > instance-metadata.json
```


## Problem 1: Working with RDDs (4 points)

Amazon maintained a list of the top 1 million Internet sites by traffic at the URL (they do not anymore). A recent copy is included in this repository which you will use for this problem. 

In this problem you will:

* Make an RDD where each record is a tuple with the (rank, site)
* Determine the number representation of top-level domains (TLDs) in the top 10,000 websites. Example TLDs are `com`, `edu` and `cn`. (Do not include the `.`). 

### Place the domains file in HDFS

* Unzip the file `top-1m.csv.zip`
* Put the file `top-1m.csv` into HDFS with the command:

```
[hadoop@ip-172-31-91-222 ~]$ hadoop fs -put top-1m.csv top-1m.csv
```

Verify that the file is there with `hadoop fs -ls`.

```
[hadoop@ip-172-31-91-222 ~]$ hadoop fs -ls
Found 2 items
drwxr-xr-x   - hadoop hadoop          0 2018-03-25 18:48 .sparkStaging
-rw-r--r--   2 hadoop hadoop   23245165 2018-03-25 18:50 top-1m.csv
```

The rest of the work will be done within the [problem-1.ipynb](problem-1.ipynb) Jupyter notebook.

After you finish working on the problem, you will commit the Jupyter notebook `.ipynb` file called `problem-1.ipynb.`

## Problem 2: Working with SparkSQL (6 points)

You will perform the work for this problem within the [problem-2.ipynb](problem-2.ipynb) Jupyter notebook.

After you finish working on the problem, you will commit the Jupyter notebook `.ipynb` file called `problem-2.ipynb.`

## Submitting the Assignment

Make sure you commit **only the files requested**, and push your repository to GitHub!

The files to be committed and pushed to the repository for this assignment are:

* `instance-metadata.json`
* `problem-1.ipynb`
* `problem-2.ipynb`


## Grading Rubric 

* We will look at the results files and the scripts. If the result files are exactly what is expected, in the proper format, etc., we may run your scripts to make sure they produce the output. If everything works, you will get full credit for the problem.
* If the results files are not what is expected, or the scripts produce something different from what is expected, we will look at code and provide partial credit where possible and applicable.
* Points will be deducted for each the following reasons:
	* Instructions are not followed
	* Output is not in expected format (not sorted, missing fields, wrong delimeter, unusual characters in the files)
	* There are more files in your repository than need to be 
	* There are additional lines in the results files (whether empty or not)
	* Files in repository are not the requested filename
