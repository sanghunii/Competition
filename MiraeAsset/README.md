# MiraeAsset_Competition_Model


# 0. Title : Customized AI Reporter Service based on LLM targeting small-cap stocks 




# 1. Service proposal background

* Ordinary individual investors who only made stable investments that followed the existing market index cannot easily take on the challenge of more aggressive investment through small-cap investment. 
      -> When it comes to small-cap stocks, companies ranked 301st or lower in market capitalization in the Korean market are called small-cap stocks.



* There is several reasons
  
-> Small-cap stocks have less absolute information than large-cap stocks.

-> In addition, this information is scattered sporadically on the Internet like a dot organization.

-> Most individual investors do not invest in stocks as their main job, but instead have a separate job to make a living.

-> Therefore, investors who want to invest in small-cap stocks must collect and organize this information to be able to objectively judge the company, but              this process itself is quite burdensome for ordinary individual investors who have a separate main business.



* Therefore, we designed a service that provides comprehensive information on small stock stocks scattered sporadically on the Internet.




# 2. How to execute

1. Get the API_KEY from the website.
    
2. Register your payment method on billing section where website

3. Create .env file on working directory
    
4. Put your API_KEY on .env file / Form : _API_KEY = YOUR_API_KEY_
    
5. Compile finance_chatbot.py
    
6. At first, a predetermined question form is created and passed to the model, and an answer is generated accordingly.

   -> To ensure that even people with no knowledge of stocks or the relevant items receive basic answers with some quality
        
7. Ask additional question and receive answer.
    
8. If you put only '#' on prompt, conversation is end.



# 3. If you Execute Model with out register billing method

- You can have a conversation, but the model returns the user's question as is, rather than an answer to the user's question.



# 4. Datasets

- We use financial report and financial thesis for making finance domain specializing model.
- Datasets are supplied by _AI_HUB_ https://www.aihub.or.kr
- Datasets folder must be located in the same working directory as model code files. (See Below)

        << data file path example >>

            -> directory_that_locate_modelcodes/datasets/finance_thesis/finance_thesis_file

