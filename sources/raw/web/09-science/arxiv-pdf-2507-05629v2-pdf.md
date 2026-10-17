# 大模型生成检索题的课堂研究

- 链接：https://arxiv.org/pdf/2507.05629v2.pdf
- 作者：Yuan An, John Liu, Niyam Acharya, Ruhma Hashmi
- 获取方式：arXiv 摘要 + HTML 全文

---

## 摘要

Retrieval practice is a well-established pedagogical technique known to significantly enhance student learning and knowledge retention. However, generating high-quality retrieval practice questions is often time-consuming and labor intensive for instructors, especially in rapidly evolving technical subjects. Large Language Models (LLMs) offer the potential to automate this process by generating questions in response to prompts, yet the effectiveness of LLM-generated retrieval practice on student learning remains to be established. In this study, we conducted an empirical study involving two college-level data science courses, with approximately 60 students. We compared learning outcomes during one week in which students received LLM-generated multiple-choice retrieval practice questions to those from a week in which no such questions were provided. Results indicate that students exposed to LLM-generated retrieval practice achieved significantly higher knowledge retention, with an average accuracy of 89%, compared to 73% in the week without such practice. These findings suggest that LLM-generated retrieval questions can effectively support student learning and may provide a scalable solution for integrating retrieval practice into real-time teaching. However, despite these encouraging outcomes and the potential time-saving benefits, cautions must be taken, as the quality of LLM-generated questions can vary. Instructors must still manually verify and revise the generated questions before releasing them to students.

## 正文

# Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses

###### Abstract

Retrieval practice is a well-established pedagogical technique known to significantly enhance student learning and knowledge retention. However, generating high-quality retrieval practice questions is often time-consuming and labor intensive for instructors, especially in rapidly evolving technical subjects. Large Language Models (LLMs) offer the potential to automate this process by generating questions in response to prompts, yet the effectiveness of LLM-generated retrieval practice on student learning remains to be established. In this study, we conducted an empirical study involving two college-level data science courses, with approximately 60 students. We compared learning outcomes during one week in which students received LLM-generated multiple-choice retrieval practice questions to those from a week in which no such questions were provided. Results indicate that students exposed to LLM-generated retrieval practice achieved significantly higher knowledge retention, with an average accuracy of 89%, compared to 73% in the week without such practice. These findings suggest that LLM-generated retrieval questions can effectively support student learning and may provide a scalable solution for integrating retrieval practice into real-time teaching. However, despite these encouraging outcomes and the potential time-saving benefits, cautions must be taken, as the quality of LLM-generated questions can vary. Instructors must still manually verify and revise the generated questions before releasing them to students.

*K*eywords Retrieval practice  $\cdot$
large language models  $\cdot$
generative AI  $\cdot$
student learning  $\cdot$
multiple-choice questions  $\cdot$
STEM education  $\cdot$
data science  $\cdot$
higher education

## 1 Introduction

Retrieval practice \[30\], frequently termed the “testing effect” \[3\], is a teaching technique that has been extensively studied. Empirical evidence has clearly indicated its ability to enhance long-term memory retention and overall learning \[29, 3, 24, 27, 18, 2\]. This technique involves the active recall of information from memory, a process that inherently strengthens neural connections and improves the future retrieval of that information. The historical roots of retrieval practice can be traced back to the observations of Francis Bacon in 1620 \[37\] and William James in 1890 \[37\]. Modern experimental studies were conducted in the early 20th century through the pioneering work of researchers such as Abbott (1909) \[1\] and Gates (1917) \[13\].

It was not until the 21st century, nearly 100 years later, that retrieval practice gained popularity among educators as a teaching strategy \[4\]. Roediger and Karpicke \[29, 16, 27\] has consistently demonstrated the effectiveness of retrieval practice over alternative study methods, including concept mapping or repeated reading. Using retrieval practice proves effective across diverse age groups and subject domains, and its benefits extend to improvement of higher-order thinking. Furthermore, retrieval practice has been shown to improve metacognition. Students are better able to identify gaps in their knowledge and direct their study efforts more effectively.

Concrete Retrieval Practice Activities.
Retrieval practice can be integrated into classrooms through a
range of in-class activities, such as *warm-up quizzes, live polling,
multiple-choice questions (MCQs), think–pair–share, one-minute write-ups,
concept mapping from memory*, and *brain dumps*.
In a college-level data science programming course, for example,
an instructor might pose the following low-stakes MCQ
that prompts students to recall and apply key programming concepts:

Question:"Which of the following Python code snippets correctly calculates the mean of the columns of a pandas DataFrame while ignoring missing values (NaNs)?"

Answers (Choose one):

(a) data.mean();

(b) data.mean(axis=0);

(c) np.mean(data);

(d) data.mean(axis=1);

This question requires students to retrieve, from their memory, not only the correct function but also the appropriate parameter for handling dimensional directions, a common task in data science workflows. By regularly engaging in such low-stakes retrieval activities, students can reinforce their understanding of programming syntax and behavior, potentially leading to better learning outcomes.

### 1.1 Challenges of Applying Retrieval Practice in Real-Time Teaching

Despite the well-documented benefits of retrieval practice, there are significant challenges for instructors to implement them, in particular, during live teaching. A primary challenge is the inherently time-consuming and labor-intensive nature of generating high-quality, contextual, and appropriately challenging retrieval practice questions. This challenge is particularly evident in rapidly evolving technical fields such as Data Science, where course content is quickly updated, and the instructor needs to come up with a set of new retrieval practice each time the course is taught.

Another challenge is to dynamically generate retrieval practices that achieve what is pedagogically known as ”desirable difficulty”. Effective retrieval practices not only recall factual knowledge, but also access higher-order thinking skills. During real-time teaching, it is necessary to adjust the level of difficulties based on students’ performance. If a previous activity is too easy, the subsequent practice should be made progressively more challenging, and vice versa.

### 1.2 The Transformative Potential of Large Language Models (LLMs)

Large language models (LLMs) such as OpenAI’s GPT and Google’s Gemini offer excellent capabilities in natural language understanding and generation. These sophisticated models are engineered to process vast quantities of text data. By analyzing various linguistic patterns, LLMs are able to generate coherent, contextually appropriate content. For educational purposes, LLMs hold significant potential to automate a variety of tasks, for example, generating retrieval practice questions based on relevant course materials. The automation capability can significantly reduce the burden on instructors, enabling them to focus more on course planning, delivering, and student engagement.

### 1.3 Contributions of This Study

While the capabilities of LLMs in generating educational content are increasingly recognized, empirical evidence specifically examining the impact of LLM-generated retrieval practice questions on actual student learning outcomes within higher education, particularly in STEM fields, remains largely underexplored. Existing preliminary research presents mixed results, with many studies primarily focusing on the quality of question generation rather than the direct impacts on student learning \[25, 12\]. This indicates a critical need for rigorous investigation into the practical benefits of integrating LLMs into core teaching practices.

In this study, we attempt to bridge the gap. We empirically investigate whether the administration of LLM-generated multiple-choice retrieval practice questions would enhance student learning outcomes. We conduct the research in college-level Data Science courses which cover data science programming in Python and cloud computing technology.

Summary and Contributions: Each course lasted 10 weeks in a quarter system. We conducted the experiments in weeks 6-9, a total of 4 weeks. Each experiment consisted of a 2-week cycle. In the first week of each cycle, students were either exposed to LLM-generated retrieval practice questions or received no retrieval practice. In the second week of each cycle, we assessed students’ knowledge rentention with a set of quizzes. The results clearly indicated that when students were exposed to LLM-generated retrieval practice, they achieved an average accuracy of 89% in the assessment quiz. If students received no retrieval practice, they only achieved an averagy accuray of 73%.

This study provides a piece of empirical evidence for the effectiveness of LLM-generated retrieval practice questions in a real-world higher education setting. It demonstrates a practical and scalable solution to the time-consuming of applying an effective technique for real-time STEM teaching.

The remainder of the paper is organized as follows. Section 2 reviews related work on using LLMs for multiple-choice question (MCQ) generation and evaluating their impact. Section 3 outlines the study methodology and experimental design. Section 4 presents the results of the study. Section 5 discusses practical issues and limitations of the study. Finally, Section 6 discusses future directions and concludes the paper.

## 2 Related Work

We review the related work in the following sub topics:
*the effectiveness of retrieval practice,
automatic generation of MCQs using LLMs*,
*empirical studies on LLM-generated educational assessments*,
and *LLM application in broader
educational support and assessment*.

### 2.1 The Effectiveness of Retrieval Practice

The effectiveness of retrieval practice is highlighted by several key cognitive mechanisms, extensively studied in educational psychology \[30, 15, 29, 3, 24, 27, 18, 2\]. This fundamental phenomenon illustrates that the active retrieval of information from memory significantly enhances long-term retention more effectively than passive re-studying. It is recognized not merely as an assessment tool but as a powerful teaching strategy \[5\]. To achieve the desirable difficulties in retrieving memory, retrieval practice questions should be designed with spacing \[33, 19, 10, 22, 36\] and interleaving \[31, 34, 32, 28, 26\].

### 2.2 Automatic Generation of Multiple-Choice Questions (MCQs) using LLMs

LLMs have been utilized to generate multiple-choice questions (MCQs) across a range of subjects. An empirical study by Olney \[25\] reported no significant differences between human-authored and LLM-authored MCQs when evaluated by medical experts for an anatomy and physiology textbook. This suggests a baseline level of quality can be achieved. Doughty et al. in \[12\] demonstrated that LLMs could produce high-quality programming MCQs aligning with learning objectives. Maity et al. in \[21\] studied a novel multi-stage promting (MSP) approach to generate zero-shot and one-shot MCQs in multiple human languages (English, German, Hindi, Bengali) without fine-tuning. Tran et al in \[35\] found that GPT-4 significantly outperformed GPT-3 in generating isomorphic MCQs for computing courses, correctly producing answers for 78.5% of questions compared to GPT-3’s 30.8%-36.7%. While promising, some generated MCQs still contained multiple correct choices among distractors. Lee et al. in \[17\] generated English reading comprehension questions with high validity and reliability using ChatGPT. Biancini et al. in \[8\] also compared different LLMs for generating MCQs. Maity et al. in \[20\] investigated LLM’s ability to generate questions align with different cognitive levels of Bloom’s Revised Taxonomy.

Addressing the generation of plausible and high-quality incorrect options (distractors) for MCQs is a particular challenge for assessment design. The survey in \[7\] indicated that, despite advancements, challenges remained in ensuring plausibility, reliability, and diversity, with issues like hallucination and bias persisting. McNichos et al. in \[23\] showed that in-context learning with selected examples was more effective than random or zero-shot baselines for math MCQs. Bitew et al. in \[9\] demonstrated that ChatGPT-driven solutions could produce high-quality distractors and were more reliable, generating significantly fewer ”nonsense distractors” compared to traditional ranking-based models.

Extensions to theses studies include developing advanced LLM techniques to generate distractors that accurately reflect common student misconceptions rather than just arbitrary incorrect options, creating more sophisticated reference-free metrics for evaluating distractor quality to better capture their pedagogical effectiveness, further exploring the automated generation of informative feedback messages for each distractor, and explaining why an option is incorrect and guiding students toward the correct understanding.

### 2.3 Empirical Studies on LLM-Generated Educational Assessments

The empirical investigation in \[38\] by Witsken et al. found that while students could not discern whether questions were LLM-authored or human-authored, student scores on LLM-authored questions were almost 9% lower. This outcome could indicate subtle differences in difficulty or styles that might impact student performance, even if the questions are deemed “well-composed and relevant” by human reviewers.

Another empirical study in \[39\] by Yusof compared the final exam scores between previous cohorts who did not use ChatGPT for retrieval practice (control group) and current cohorts who did (experimental group). The study reported significantly better final exam scores for students in the experimental group. The primary sample consisted of second-year education students enrolled in the Measurement and Evaluation in Education course, with 64 students randomly selected for each group. The study also highlighted the need of human monitoring and judgment for addressing complex learning needs and provide deeper contextual understanding.

### 2.4 LLM Application in Broader Educational Support and Assessment

LLMs are also applied to a wider array of educational tasks beyond the direct generation of questions, including pedagogical support, content creation, and general educational research. Hu et al. in \[14\] demonstrated that LLMs (GPT-4, Claude 3.5 Sonnet) could significantly enhance the quality of teaching plans. This was achieved through a multi-stage process involving simulating teacher-student interactions, generating teaching reflections, and iteratively refining the original teaching plan based on these simulated insights. Das et al. in \[11\] surveyed broadly on automatic question generation and answer assessment in online learning. It highlighted challenges in assessing subjective questions and the need for standardized evaluation procedures.

Despite these developments and advancements in various educational aspects, there remains a need for more empirical studies, particularly in STEM fields, to rigorously assess the effectiveness of LLM-generated content for retrieval practice activities.

## 3 Methodology

Our investigation is motivated by the following research question:
*Does frequent use of LLM-generated MCQs as retrieval practice during
real-time STEM instruction improve student knowledge retention?* To answer this
question, we implement a quasi-experiment within real classroom environments.

### 3.1 Study Design: A Quasi-Experimental Approach

While true experiments, characterized by random assignment, are ideal for evaluating the effect of the intervention, i.e., LLM-generated MCQs, their implementation is impractical in real-world classrooms. It is difficult to randomly assign students of the same live lecture to different intervention groups without introducing performance bias due to lack of blinding. A quasi-experimental design, by contrast, enhances the practical relevance of the study’s conclusions for real-world and authentic context.

Specifically, we utilize a non-equivalent groups design, wherein pre-existing student groups were compared, rather than relying on random individual assignment. Students within the same course assigned to different conditions in different sections. In one section, students receives the intervention (e.g., LLM-generated MCQs as retrieval practice), and the other does not. We compare the outcomes (e.g., knowledge retention) over time to infer the intervention’s effect.

However, it is important to acknowledge the inherent limitations of quasi-experimental designs regarding internal validity when compared to true experiments. The absence of true random assignment means that unmeasured confounding variables could potentially influence the observed effects, as pre-existing differences between sections cannot be entirely ruled out.

### 3.2 Participants and Context

The study cohort comprised approximately 60 undergraduate students enrolled in two college-level courses in an undergraduate data science program. Both courses address rapidly evolving technical domains, requiring students to develop strong conceptual understanding and long-term retention in these domains. Each course lasted 10 weeks in a quarter system.

### 3.3 Implementation of the Study

The empirical investigation was conducted over a total of four weeks, specifically weeks 6-9 of the 10-week quarter system for both courses, named as course1 and course2. The experiment was structured into two distinct 2-week cycles.

#### 3.3.1 First Cycle (Weeks 6-7): LLM-Enhanced Retrieval Practice Condition

Week 1 of First Cycle (Week 6 in the quarter): The students in course1 and course2 were taught using their respective content. Each course included two lectures, each lasting 120 minutes. The instructor deliberately divided each lecture into 10–15-minute segments. At the end of each segment, students were asked to answer multiple-choice questions (MCQs) generated by an LLM as a form of retrieval practice. Immediate feedback on the correctness of responses was provided to students after each attempt. The retrieval practice activities were explicitly designed as low-stakes learning opportunities. Students could try the retrieval practice as many times as they want.

Week 2 of First Cycle (Week 7 in the quarter): The students in both courses took a comprehensive quiz (Quiz 1), respectively. The quiz covered the material presented in Week 1 of this cycle.

#### 3.3.2 Second Cycle (Weeks 8-9): Control Condition (No Retrieval Practice)

Week 1 of Second Cycle (Week 8 in the quarter): The students in course1 and course2 were taught with their respective content across both lectures. They were allowed to review the lecture materials and re-study the content independently. However, no retrieval practice activities were incorporated during the live lectures.

Week 2 of Second Cycle (Week 9 in the quarter): The students in both courses took another comprehensive quiz (Quiz 2) covering the material presented in Week 1 of this second cycle.

The online platform used for the delivery of MCQs and quizzes was Google form.

### 3.4 Generating MCQs Using LLM

Our experiment was conducted from March to June 2025. During this period, we accessed the free versions of ChatGPT (GPT-3.5 and GPT-4o) and Google AI Studio (Gemini 2.0 and 2.5 Flash). After initial comparisons of MCQs generated from the same lecture materials across multiple rounds, we did not observe significant differences between the applications. Consequently, we primarily used Google AI Studio for MCQ generation in the experiments.

Course Materials: The teaching of both courses was delivered through Jupyter notebooks. We strategically placed breaks roughly every 10-15 minutes within the notebooks for retrieval practice activities. For the purpose of generating MCQs, each notebook’s content was converted into markdown text, and the relevant sections were injected into the AI prompts.

Prompt Engineering: To ensure the generation of high-quality, contextually relevant, and pedagogically sound multiple choice questions (MCQs), we iteratively crafted the following prompt:

```
    ### System Instruction ###
    You are an expert college course instructor teaching data science
    programing and cloud computing. Your task is to create high-quality,
    pedagogically sound multiple choice questions (MCQs) based on the
    course content provided below. Create these MCQs that test:
    1. Factual recall: checking students’ understanding of specific
       concepts or facts.
    2. Higher-order thinking: such as application, analysis, or
       evaluation.
    Each MCQ must:
    - Include one correct answer and three plausible distractors.
    - Avoid using clues or phrasing in the question stem that would
      directly give away the correct answer.
    - Ensure that all answer options are grammatically parallel,
      plausible, and contextually relevant.
    - Mix the cognitive level across questions: some should be direct,
      others should require critical thinking.
    Output Each MCQ in the Following Format:
        Question: [Insert question here]
        Options (One Correct Answer):
            (a) Option A
            (b) Option B
            (c) Option C
            (d) Option D
        Correct Answer: [A/B/C/D]
        Explanation: [Brief explanation of why it’s correct, and why
        distractors are incorrect.]
    ### User Instruction ###
    Generate at least 15 MCQs based on the following course content.
    """
    {Insert course content here}
    """
```
The generated MCQs will undergo the following quality assurance checks:

- • 
Ensuring questions accurately reflected the provided lecture content and aligned with learning objectives.
- • 
Verifying that questions and their respective options were clearly formulated and unambiguous.
- • 
Confirming that the designated correct answer was indeed accurate and sound.
- • 
Assessing that incorrect options (distractors) were plausible and challenging enough to test understanding, preventing easy identification of the correct answer.
- • 
Ensuring questions assessed a range of cognitive levels, from basic factual recall to high-order thinking
- • 
Verifying that questions contained no hallucinations.

As we will discuss in Section 5, while LLMs offer significant scalability, sometimes they still produce low-quality MCQs. Currently, human-in-the-loop validation is a critical component before the instructor release the MCQs to students.

### 3.5 Data Collection and Statistical Analysis

Data Points: For each course, data were collected during the second week of each cycle through quizzes. Quiz 1, administered in the first cycle, was conducted under the LLM retrieval practice condition, whereas Quiz 2, administered in the second cycle, served as the control condition with no LLM-generated MCQs used for retrieval practice. The primary data collected for analysis were student quiz scores, measured as the percentage of correct answers for each participant on both Quiz 1 and Quiz 2. We then combined the results of Quiz 1 from both courses into a single list. Similarly, the results of Quiz 2 from both courses were merged into another list.

Statistical Analysis: The lengths of the two datasets differ due to variations in course attendance and student response. However, we ensured that most of the students remained the same, in particular, for cycle 1. In addition, the quizzes were administered anonymously, so the participants could be treated as independent groups. An appropriate statistical test will be conducted to determine whether there was a statistically significant difference in the results between Quiz 1 and Quiz 2.

- • 
*Assumptions:* Prior to conducting the test, we will check the
distributions of the difference scores between the two quizzes.  
A p-value of $\leq 0.05$ is predetermined as the threshold for statistical significance.
- • 
*Effect Size:* In addition to statistical significance, effect size will be
calculated to quantify the practical magnitude of the observed difference in scores.
This measure provides a clearer understanding of how large the difference between
the quiz scores truly is, independent of sample size. Effect size would illustrate
the real-world impact rather than just the likelihood of the difference occurring by chance.

## 4 Results

Figure 1 (a) and Figure 1 (b) show the score distributions of Quiz 1 and Quiz 2, respectively. The visualization indicates that the scores are skewed and not normally distributed. Also, the two lists have different lengths. By these observations, we conduct Mann-Whitney U test which is non-parametric and compares the medians. A common effect size measure for the Mann-Whitney U test is $r$ or rank-biserial correlation. This effect size measures the proportion of times a randomly selected observation from one list is larger than a randomly selected observation from the other list, minus the reverse proportion.

In essence,

- • 
The Mann-Whitney U test answers the question: "Is there a statistically significant tendency for scores in one quiz to be higher than scores in the other?"
- • 
The rank-biserial correlation $r$ answers the question: "How large is this tendency or difference in distributions?" A larger r (between -1 and 1) value indicates a greater degree of separation or difference between the distributions of scores from the two quizzes.

Table 1 shows the results of the Mann-Whitney U test. The value of U statistics is 703 which is closer to $n1*n2=837$. The larger value suggests less overlap in the ranks, indicating a greater separation between the two groups. The small p-value indicates that we have sufficient evidence to conclude that there is a statistically significant difference in the distributions of scores between the two quizzes.

This finding, combined with the large positive Z-score (4.4627), the large positive rank-biserial correlation (r = 0.5860), and the descriptive statistics showing a much higher median and mean for Quiz 1, provides very strong evidence that students performed significantly better on Quiz 1 than on Quiz 2. The observed difference is highly unlikely to be due to random chance.

| Item | Results | 
|---|---|
| The Mann-Whitney U test: | U Statistic: 703.0000 | 
|  | P-value \< 0.0001 | 
| Effect Size: | Sample size Quiz 1 (n1): 31 | 
|  | Sample size Quiz 2 (n2): 27 | 
|  | Total sample size (N): 58 | 
|  | Approximate Z-score: 4.4627 | 
|  | Rank-Biserial Correlation (r): 0.5860 | 
| Quiz 1 Scores: | mean: 0.89 | 
|  | std: 0.13 | 
|  | median: 0.95 | 
| Quiz 2 Scores: | mean: 0.73 | 
|  | std: 0.15 | 
|  | median: 0.75 | 

## 5 Discussion

The statistical analysis on scores from Quiz 1 and Quiz 2 revealed that the students achieved significantly better learning outcomes if they practiced with LLM-generated MCQs, compared to a time when they did not perform any retrieval practice. Although LLMs present a scalable solution for instructors to incorporate retrieval practice activities into live teaching, some practical considerations exist. In this section, we discuss the common quality issues of the LLM-generate MCQs and the limitations of the study.

### 5.1 Quality Issues of the LLM-Generated MCQs

We have been using LLMs to generate various assessment materials since ChatGPT appeared
in Nov. 2022. Our experience has shown that the quality of LLM-generated content
varies significantly depending on LLM, prompt design, and knowledge injection. Human
verification and validation is indispensable. For example, we always presented 5 MCQs as retrieval
practice for every 10-15-minute lecture. To choose 5 high-quality MCQs, we typically had to ask
the LLM to generate at least 15 MCQs based on given course content. There were about 2/3 of the
LLM-generated MCQs which did not meet our objectives. These low-quality MCQs can be categorized
into following issues: *(1) question and options containing mistakes, (2) hallucinations,
(3) question containing hints to answers, (4) duplicated options, (5) ambiguous answers,
(6) easy distractors, (7) trivial knowledge, (8) inconsistent formats of options, (9) only negations
in distractors*, *(10) double-concept questions, (11) incorrect assumption*,
and , *(12) ambiguous question*. In the following, we
illustrate each issue using an example we have encountered. Note that the MCQ examples below
were generated by an LLM based on the course materials injected in the prompt.

1\. Question and options containing mistakes. LLMs generate incorrect MCQs from time to time. For example, when we extract a subset of a 2-D numpy array, we can use either positive indices counting from 0 or negative indices counting from -1 backwardly. The LLM struggled in reasoning about negative indices. Here is an example with mistakes:

```
    Question: "What is the result of slicing arr[-3:, :-1]
    where arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])?"
    Options (One Correct Answer):
        (a) [[7, 8], [4, 5]]
        (b) [[1, 2], [7, 8]]
        (c) [[4, 5], [7, 8]]
        (d) [[7, 8], [4, 5], [1, 2]]
```
Based on the course materials we taught in the lecture, the correct answer is \[\[1, 2\], \[4, 5\], \[7, 8\]\]. But after we injected the course materials to the LLM, the options generated by the LLM do not contain the correct answer. The LLM reasoned about the content incorrectly.

2\. Hallucinations. LLMs may generate question and options that contain concepts which do not exist in the course materials. For example, the following MCQ contains the attribute arr.rank. However, the lectures never mentioned the attribute arr.rank. The LLM made up such a concept in the MCQ question.

```
    Question: "The arr.rank attribute returns the number of axes
    in a NumPy array."
    Options (One Correct Answer):
        (a) True
        (b) False
        (c) Only if arr.shape is not defined
        (d) Only in NumPy v2.0+
```
3\. Question containing hints to answers. LLMs may generate a question that contains a hint to the correct answer. For example, in the following MCQ, the hint ’What is Spark’ is contained in the question.

```
    Question: "What is the name of the unified analytics engine for
    big data processing that is mentioned in the ‘What is Spark?’ section?"
    Options (One Correct Answer):
        (a) Hadoop
        (b) Spark
        (c) Flink
        (d) MapReduce
```
4\. Duplicated options. LLMs may generate MCQs that have duplicated options. For example in the following MCQ, the options (c) and (d) are duplicated because the words “mean” and “average” have the same meaning.

```
    Quesiton: "What does np.mean(arr, axis=1) compute when
    arr is a 2D array?"
    Options (One Correct Answer):
        (a) The mean of all elements
        (b) The mean of each row
        (c) The mean of each column
        (d) The average of each column
```
5\. Ambiguous answers. LLMs may generate MCQs that have ambiguous answers. For example, in the following MCQ, the options (c) and (d) are ambiguous. Either one could be a correct answer given some reasonable explanation.

```
    Question: "What is the cost function used for training logistic
    regression models?"
    Options (One Correct Answer):
        (a) Sigmoid function
        (b) Gradient function
        (c) Log likelihood function
        (d) Cross-entropy function.
```
6\. Easy distractors. LLMs may generate MCQs that provide one correct option and three easy distractors. For example, the distractors of the following MCQs can be discerned without much knowledge about the content.

```
    Question: "What does arr.reshape(2, 3) do to a 1D array of 6 elements?"
    Options (One Correct Answer):
        (a) Changes its shape to 2 rows and 3 columns
        (b) Removes the last 3 elements
        (c) Sorts the array
        (d) Adds padding to reach a 2x3 shape
```
7\. Trivial knowledge. LLMs may generate MCQs that are trivial for factual recall. For example, the following MCQ asks a trivial question.

```
    Question: "Which property returns the shape of a NumPy array?"
    Options (One Correct Answer):
        (a) ndim
        (b) size
        (c) shape
        (d) dtype
```
8\. Inconsistent formats of options. LLMs may generate MCQs with inconsistently formatted options that make the correct answer easily identifiable. For example, in the following MCQ, the correct option is significantly longer than the distractors, making it stand out.

```
    Questions: "What is the primary reason that single machines can
    struggle with large-scale data processing?"
    Options (One Correct Answer):
        (a) Lack of available memory
        (b) Slow network connection
        (c) Not enough hard drive space
        (d) Single machines often lack the sufficient processing power
            and resources, as well as the speed required, to efficiently
            perform computations on the vast amounts of information that
            characterize big data, leading to prohibitively long
            computation times.
```
9\. Only negations in distractors. LLMs may generate MCQs in which all distractor options contain negations, while the correct answer does not. For example, the following MCQ has such a pattern that makes it easy identify the correct answer simply by recognizing the difference in phrasing, rather than understanding the content.

```
    Question: "What is true about sequential feature selection algorithms?"
    Options (One Correct Answer):
        (a) They reduce the feature space step-by-step using a
            performance criterion
        (b) They do not consider classification performance while
            reducing features
        (c) They avoid using greedy search methods
        (d) They never remove features from the original set
```
10\. Double-concept questions. LLMs may generate MCQs that contain multiple concepts in the description causing confusion. For example, the following MCQ describes disconnected parts in the question with insufficient context.

```
    Question: "According to the text, overfitting is characterized by high
    variance and can be addressed by regularization. However, if a model is
    suffering from underfitting , what action would generally be more
    appropriate based on the principles discussed?
    Options (One Correct Answer):
        (a) Reduce regularization
        (b) Increase regularization
        (c) Add more data
        (d) Add more features
```
11\. Incorrect Assumption. LLMs may generate MCQs by making incorrect assumptions. For example, in the following MCQ, the LLM assumed that the order of steps mentioned in the lecture was the only one that is correct. However, the order was just suggested by the API. The LLM assumed that the suggested one was the only one by using the phrase ”the correct order of steps.”

```
    Question: "According to the Scikit-Learn estimator API, which of the
    following is the correct order of steps?"
    Options (One Correct Answer):
        (a) 1. Fit the model, 2. Choose model, 3. Arrange data,
            4. Apply the Model
        (b) 1. Choose model, 2. Choose hyperparameters, 3. Arrange data,
            4. Fit the model, 5. Apply the Model
        (c) 1. Arrange data, 2. Choose model, 3. Choose hyperparameters,
            4. Fit the model, 5. Apply the Model
        (d) 1. Arrange data, 2. Fit the model, 3. Apply the Model,
            4. Choose model, 5. Choose hyperparameters
```
12\. Ambiguous Question. LLMs may generated MCQs that have ambiguous questions. For example, the following question does not refer to the context in the course materials. Additionally, the term ’feature’ is ambiguous since it could refer to names or data.

```
    Question: "What data structure is most often used to contain
    the features?"
    Options (One Correct Answer):
        (a) Pandas Series
        (b) Python List
        (c) NumPy array or Pandas DataFrame
        (d) Python Dictionary
```
### 5.2 Limitations of the Current Study

Although the results support the hypothesis that LLM-generated retrieval practice questions significantly enhance student learning outcomes, there are several limitations in the current study. The first limitation is the quasi-experimental design. Confounding variables such as the differences between course materials in different sections could potentially influence the observed results. Secondly, the study involved a relatively small sample size. The generalizability of these findings to other academic disciplines, larger student populations, or different educational levels (e.g., K-12) may therefore be limited.

Furthermore, the assessment was conducted in 2-week cycles, measuring relatively short-term knowledge retention. We also used exclusively multiple-choice questions (MCQs) for retrieval practice. Other types of questions such as short-answer questions, or more complex problem-solving tasks could have deeper impacts. In addition, we did not measure student perceptions of the LLM-generated MCQs or their overall learning experience with the intervention. Finally, we did not measure the time and effort required for human validation.

Some ethical considerations include responsible AI integration into classroom, instructor training, bias reduction, and maintaining the development of critical-thinking and complex problem-solving skills.

## 6 Conclusion

This empirical study provides a piece of evidence demonstrating that integrating LLM-generated retrieval practice questions into higher education STEM courses significantly improves student learning outcomes. Students exposed to LLM-generated multiple-choice questions (MCQs) achieved a 16-percentage-point higher quiz accuracy (89% vs. 73%) compared to a control group. This observed difference was not only statistically significant but also practically meaningful, indicating a substantial positive impact of LLMs on learning.

The study encourages us to actively explore and develop an AI-powered lecture assistant (AILA) system \[6\] that can automatically detect a favorite moment for intervention. Future research directions include (1) automatic quality control of the LLM-generated retrieval practice questions, (2) studying the impacts of such a AI-powered lecture assistant (AILA) system on students long-term retention in diverse teaching environments, and (3) investigating the instructor’s perceptions and engagement in using such a AI-powered lecture assistant (AILA) system during course preparation and live teaching.

## References

- \[1\] Abbott, E. E. On the analysis of the factors of recall in the learning process. Psychological Monographs: General and Applied 11, 1 (1909), 159–177.
- \[2\] Agarwal, P. Retrieval practice and bloom’s taxonomy: Do students need fact knowledge before higher order learning? Journal of Educational Psychology 111, 2 (2 2019), 189–209.
- \[3\] Agarwal, P., Karpicke, J., Kang, S., Roediger, H., and Mcdermott, K. Examining the testing effect with open‐ and closed‐book tests. Applied Cognitive Psychology 22, 7 (2008), 861–876.
- \[4\] Agarwal, P. K. Personal reflections on science communication and sharing retrieval practice research with teachers. Educational Psychology Review 36, 1 (2024), 3.
- \[5\] Agarwal, P. K., and Bain, P. M. Powerful Teaching: Unleash the Science of Learning. United Kingdom: Wiley, ISBN-13:978-1119521846, 2019.
- \[6\] An, Y., Kolanupaka, S., An, J., Ma, M., Chhatwal, U., Kalinowski, A., Rogers, M., and Smith, B. Is the lecture engaging? lecture sentiment analysis for knowledge graph-supported intelligent lecturing assistant (ila) system. In 2024 IEEE International Conference on Big Data (BigData) (2024), IEEE, pp. 3358–3366.
- \[7\] Awalurahman, H. W., and Budi, I. Automatic distractor generation in multiple-choice questions: a systematic literature review. PeerJ Computer Science 10 (2024), e2441.
- \[8\] Biancini, G., Ferrato, A., and Limongelli, C. Multiple-choice question generation using large language models: Methodology and educator insights. In Adjunct Proceedings of the 32nd ACM Conference on User Modeling, Adaptation and Personalization (2024), pp. 584–590.
- \[9\] Bitew, S. K., Deleu, J., Develder, C., and Demeester, T. Distractor generation for multiple-choice questions with predictive prompting and large language models. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (2023), Springer, pp. 48–63.
- \[10\] Cepeda, N., Vul, E., Rohrer, D., Wixted, J., and Pashler, H. Spacing effects in learning: A temporal ridgeline of optimal retention. Psychological Science 19, 11 (11 2008), 1095–1102.
- \[11\] Das, B., Majumder, M., Phadikar, S., and Sekh, A. A. Automatic question generation and answer assessment: a survey. Research and Practice in Technology Enhanced Learning 16, 1 (2021), 5.
- \[12\] Doughty, J., Wan, Z., Bompelli, A., Qayum, J., Wang, T., Zhang, J., Zheng, Y., Doyle, A., Sridhar, P., Agarwal, A., et al. A comparative study of AI-generated (GPT-4) and human-crafted MCQs in programming education. In Proceedings of the 26th Australasian Computing Education Conference (2024), pp. 114–123.
- \[13\] Gates, A. I. Recitation as a factor in memorizing. Archives of Psychology 6, 40 (1917), 1–104.
- \[14\] Hu, B., Zhu, J., Pei, Y., and Gu, X. Exploring the potential of llm to enhance teaching plans through teaching simulation. npj Science of Learning 10, 1 (2025), 7.
- \[15\] Karpicke, J., and Roediger, H. Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. Journal of Experimental Psychology: Learning, Memory, and Cognition 33, 4 (7 2007), 704–719.
- \[16\] Karpicke, J. D., Butler, A. C., and Roediger III, H. L. Metacognitive strategies in student learning: do students practise retrieval when they study on their own? Memory 17, 4 (2009), 471–479.
- \[17\] Lee, U., Jung, H., Jeon, Y., Sohn, Y., Hwang, W., Moon, J., and Kim, H. Few-shot is enough: exploring chatgpt prompt engineering method for automatic question generation in english education. Education and Information Technologies 29, 9 (2024), 11483–11515.
- \[18\] Lyle, K., and Crawford, N. Retrieving essential material at the end of lectures improves performance on statistics exams. Teaching of Psychology 38, 2 (3 2011), 94–97.
- \[19\] Maddox, G. Understanding the underlying mechanism of the spacing effect in verbal learning: a case for encoding variability and study-phase retrieval. Journal of Cognitive Psychology 28, 6 (5 2016), 684–706.
- \[20\] Maity, S., Deroy, A., and Sarkar, S. How effective is gpt-4 turbo in generating school-level questions from textbooks based on bloom’s revised taxonomy?, 2024. URL: https://arxiv. org/abs/2406.15211.
- \[21\] Maity, S., Deroy, A., and Sarkar, S. A novel multi-stage prompting approach for language agnostic mcq generation using gpt. In European conference on information retrieval (2024), Springer, pp. 268–277.
- \[22\] Mcdaniel, M., Agarwal, P., Huelser, B., Mcdermott, K., and Roediger, H. Test-enhanced learning in a middle school science classroom: The effects of quiz frequency and placement. Journal of Educational Psychology 103, 2 (5 2011), 399–414.
- \[23\] McNichols, H., Feng, W., Lee, J., Scarlatos, A., Smith, D., Woodhead, S., and Lan, A. Automated distractor and feedback generation for math multiple-choice questions via in-context learning. arXiv preprint arXiv:2308.03234 (2023).
- \[24\] Nadel, L., Hupbach, A., Gomez, R., and Newman-Smith, K. Memory formation, consolidation and transformation. Neuroscience and Biobehavioral Reviews 36, 7 (8 2012), 1640–1645.
- \[25\] Olney, A. M. Generating Multiple Choice Questions from a Textbook: LLMs Match Human Performance on Most Metrics. In Proceedings of Empowering Education with LLMs—The Next-Gen Interface and Content Generation (July 2023), Tokyo, Japan.
- \[26\] Pan, S. The interleaving effect: Mixing it up boosts learning. Scientific American (2015).
- \[27\] Roediger, H., Agarwal, P., Mcdaniel, M., and Mcdermott, K. Test-enhanced learning in the classroom: Long-term improvements from quizzing. Journal of Experimental Psychology: Applied 17, 4 (2011), 382–395.
- \[28\] Roediger, H., and Desoto, K. Forgetting the presidents. Science 346 (2014), 1106–1109.
- \[29\] Roediger, H., and Karpicke, J. Test-enhanced learning: Taking memory tests improve long-term retention. Psychological Science 17, 3 (3 2006), 249–255.
- \[30\] Roediger, H. L., and Butler, A. C. The critical role of retrieval practice in long-term retention. Trends in cognitive sciences 15, 1 (2011), 20–27.
- \[31\] Rohrer, D. Interleaving helps students distinguish among similar concepts. Educational Psychology Review 24, 3 (7 2012), 355–367.
- \[32\] Rohrer, D., Dedrick, R., and Stershic, S. Interleaved practice improves mathematics learning. Journal of Educational Psychology 107 (2015), 900–908.
- \[33\] Rohrer, D., and Taylor, K. The effects of overlearning and distributed practise on the retention of mathematics knowledge. Applied Cognitive Psychology 20, 9 (2006), 1209–1224.
- \[34\] Taylor, K., and Rohrer, D. The effects of interleaved practice. Applied Cognitive Psychology 24, 6 (2010), 837–848.
- \[35\] Tran, A., Angelikas, K., Rama, E., Okechukwu, C., Smith, D. H., and MacNeil, S. Generating multiple choice questions for computing courses using large language models. In 2023 IEEE Frontiers in Education Conference (FIE) (2023), IEEE, pp. 1–8.
- \[36\] Uner, O., and Roediger, H. The effect of question placement on learning from textbook chapters. Journal of Applied Research in Memory and Cognition 7, 1 (2017), 116–122.
- \[37\] Wikipedia contributors. Testing effect — wikipedia, the free encyclopedia, 2024. Accessed: 2025-06.
- \[38\] Witsken, G., Crk, I., and Gultepe, E. Llms in the classroom: Outcomes and perceptions of questions written with the aid of ai. In Proceedings of the AAAI Conference on Artificial Intelligence (2025), vol. 39, pp. 27698–27705.
- \[39\] Yusof, I. J. Chatgpt-assisted retrieval practice and exam scores: Does it work? Journal of Information Technology Education: Research 24 (2025), 008.
