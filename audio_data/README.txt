README.txt

Overview
This audio data was collected for the purpose of speaker identification in 
developing country contexts. It includes a total of 83 unique voices, 35 female
and 48 male. In particular, it provides audio for performing limited vocabulary
speaker identification using digit utterances. The data was collected in
partnership with Microsoft Research India.

You can read about our work using speaker identification for 
building a low cost, remote attendance management system for developing countries
in the publication:

Hyke: A Low-cost Remote Attendance Tracking System for Developing Regions
Azarias Reda, Saurabh Panjwani and Edward Cutrell
The 5th ACM Workshop on Networked Systems for Developing Regions (NSDR 2011)

Description:
The data was collected over the telephone using an IVR (Interactive voice response)
system in March of 2011 in India. The participants are indian nationals from various backgrounds.

Each participant was given a few lines of digits, and asked
to read the numbers after getting prompted in the system. Each participant read five
lines of digits, one digit at a time. Here is an example input file given to a participant.


Line1: 26503897147819045236217896345001376258948
Line2: 02154368
Line3: 6704352918719
Line4: 0635748219561047289
Line5: 7852934016275316948052843

The numbers were all read in English. There is various levels of background noise, ranging from
faint hisses to audible conversations or songs. In total, about 30% of the audio has some level
of background noise. In general, we belive this represents an ideal dataset for many real life
speaker recognition experiments.

The data is organized in two directories, one for males and one for females. In each directory,
there is one sub-directory for each person. A person directory has the format:
        M_124534534
Where "M" indicates the sex (Male or Female), and the rest is a unique ID for the user. Under
each person directory, there are 5 audio files in WAV format. Each audio file has the format:
        124534534_N.WAV
Where "124534534" is the unique ID for the user, and "N" is which line the user is reading. In
most cases recording for line 1 (the longest) can be used for training, and the rest can be
used for testing. While we have used this for speaker identification, it can also be used for
testing 

Citation:
If you end up using this dataset, please cite the following paper:
Hyke: A Low-cost Remote Attendance Tracking System for Developing Regions
Azarias Reda, Saurabh Panjwani and Edward Cutrell
The 5th ACM Workshop on Networked Systems for Developing Regions (NSDR 2011)

Download:
To download the dataset, click here.
