from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()


model1 = ChatOpenAI()
model2 = ChatOpenAI()


prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text:\n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question-answer pairs from the following text:\n{text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document.\nNotes: {notes}\nQuiz: {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain


text = """
Support Vector Machine (SVM) is a powerful and versatile supervised machine learning algorithm that is widely used for both classification and regression tasks, with its primary strength lying in classification. The fundamental idea behind SVM is to find an optimal decision boundary, known as a hyperplane, that can effectively separate data points belonging to different classes. This hyperplane is selected in such a way that the margin, which is the distance between the hyperplane and the closest data points from each class, is maximized. These closest data points that directly influence the position and orientation of the hyperplane are known as support vectors, and they play a critical role in defining the decision boundary.

One of the most important aspects of SVM is its ability to handle both linearly separable and non-linearly separable data. For linearly separable data, SVM identifies a straight hyperplane in the original feature space, while for non-linear data, it uses a technique called the kernel trick. The kernel trick involves mapping the input data into a higher-dimensional feature space where it becomes easier to separate the classes using a hyperplane. Commonly used kernel functions include the linear kernel, polynomial kernel, and the Radial Basis Function (RBF) kernel, each suitable for different types of data patterns.

SVM is particularly effective in high-dimensional spaces and in cases where the number of features is greater than the number of samples, making it an excellent choice for text classification, bioinformatics, and image recognition tasks. It is also robust to overfitting, especially in high-dimensional spaces, because it focuses on maximizing the margin rather than fitting every point perfectly. However, choosing the right kernel and tuning hyperparameters like the regularization parameter (C) and kernel-specific parameters is crucial for achieving optimal performance. Overall, SVM remains one of the most reliable and widely used algorithms for solving complex classification problems due to its strong theoretical foundation and ability to generalize well to unseen data.
"""

intermediate = parallel_chain.invoke({'text': text})
print("\nIntermediate Output (Notes and Quiz):")
print(intermediate)


result = chain.invoke({'text': text})
print("\nFinal Merged Document:\n")
print(result)


with open("svm_notes_and_quiz.txt", "w", encoding="utf-8") as f:
    f.write(result)
print("\n✅ Output saved to svm_notes_and_quiz.txt")
