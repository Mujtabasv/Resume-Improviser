import streamlit as st
import openai


st.title('Resume Improviser')
st.header('Generates Information for Improvising your Resume.')


openai.api_key= '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'


role= st.text_input('Enter the Job Role')
job_description=st.text_input('Enter the Job Description')


def job_skill(role):
    response=openai.chat.completions.create(messages=
                               [{'role':'system','content':role,
                                 'role':'user','content':f'Give me few important skills for {role} please'}],
                               model='gpt-3.5-turbo')
    skill=response.choices[0].message.content
    return skill

skills= job_skill(role)

def pro_summ(role):
    response=openai.chat.completions.create(messages=
                               [{'role':'system','content':role,
                                 'role':'user','content':f'Give me professional summary for {role} please'}],
                               model='gpt-3.5-turbo')
    summary=response.choices[0].message.content
    return summary

summ= pro_summ(role)

def cover_letter(role):
    response=openai.chat.completions.create(messages=
                               [{'role':'system','content':role,
                                 'role':'user','content':f'Give me a cover letter for {role} please'}],
                               model='gpt-3.5-turbo')
    cover=response.choices[0].message.content
    return cover

letter= cover_letter(role)


if st.button('Generate'):
    st.text(f'Skills required for the role {role}:')
    st.success(skills)
    st.text(f'Summary(Professional) for the role {role}:')
    st.success(summ)
    st.text(f'Cover Letter for the role {role}:')
    st.success(letter)