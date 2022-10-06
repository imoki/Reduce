# 论文批量降重工具（软件名：默降重）
批量降重工具，基于paperyy的api实现一个报告降重800字，可用多个报告的降重次数对同一文本进行降重  

## 软件简要
  批量降重工具，基于paperyy的api实现一个报告降重800字的效果。  
paperyy每天有一次免费查重机会，查重后会生成报告，一份报告可以免费降重2次。  
原本每次降重都只能是软件中指定的几十字，而“批量降重工具.exe”利用2次免费降重数可对800字降重。  
通过“文本格式化工具.exe”可辅助提取paperyy中标红的待查重文字（可选的工具）。软件中包含详细说明书。

## 主要优势
1. 实现一个paperyy报告对800字降重的效果  
2. 可用多个报告的降重次数对同一文本进行降重，从而实现一次几千字的降重。  
3. 可以自由选择待降重的文本内容  

## 使用建议
1. 在待降重文本“sentence.txt”中尽量多填需要降重的文本（大于800字）  
2. 建议每天都去查重，报告记录一周内都有效，可存起来用工具统一使用降重次数。  
  因此如果你有一周的报告记录，则可以使用14次的免费降重次数，实现对5600字的降重（400字*14）  
3. 未被降重的文本会写入“notReduceSentence.txt”中，下次使用软件时可将这个文本改名为“sentence.txt”（待降重文本）进行降重  
4. 多多支持“PaperYY”，如果觉得好用请将PaperYY推荐给身边的人。  

## 使用说明
### 获取查重报告url
1. 微信小程序搜索“PaperYY论文查重”  
![1665024907174](https://user-images.githubusercontent.com/78804251/194203963-ad2cdd3b-f075-4540-aa2b-0093d970546d.jpg)  
2. 使用免费次数进行查重（注意是“查重”，每天都能免费查重一次）
<img src="https://user-images.githubusercontent.com/78804251/194204147-29f642e7-930f-44d7-9337-acfd02893510.png" width="300px" style="align: center;">  
3. 这里点击“提交查重”后界面可能没有响应，其实已经在查重了，直接返回主页就行
<img src="https://user-images.githubusercontent.com/78804251/194207719-56092bba-cc77-471d-8841-96ae44221982.png" width="300px" style="align: center;"> 
3. 点击“我的”--“查重报告”  
<img src="https://user-images.githubusercontent.com/78804251/194204250-8423af01-139c-4d7b-9138-8cf5de486580.png" width="300px" style="align: center;"> 
<img src="https://user-images.githubusercontent.com/78804251/194207922-a49bc103-ddeb-4d92-a33a-bb32777c06ae.png" width="300px" style="align: center;"> 
4. 复制报告记录url  
<img src="https://user-images.githubusercontent.com/78804251/194209685-59b65053-2813-43bd-9ed7-7e98be76019f.png" width="300px" style="align: center;"> 

### 使用降重软件
1. 将上述得到的报告记录写入repo.txt中（如果有多个记录则按行写入repo.txt中。一个记录能降重800字，可叠加使用，从而达到一次降重几千字的效果。）
<img src="https://user-images.githubusercontent.com/78804251/194205817-4227ca27-4148-4abf-a3c6-2b223d0f2ff5.png" width="500px" style="align: center;"> 
2. 将需要降重的文本写入sentence.txt文件中  
<img src="https://user-images.githubusercontent.com/78804251/194206561-23048f77-b2b0-40ff-b36c-7437b9d249c3.png" width="500px" style="align: center;"> 
3. 双击运行“批量降重工具.exe”  
<img src="https://user-images.githubusercontent.com/78804251/194206587-15b134f1-a98e-42a6-949c-46b98cca8454.png" width="500px" style="align: center;"> 
4. 若降重成功会生成reduceSentence.txt文件，里面包含降重后的内容  
<img src="https://user-images.githubusercontent.com/78804251/194206608-30e11898-6279-424d-b4b3-5e1a1c102f0e.png" width="500px" style="align: center;"> 
未降重的内容会被写入notReduceSentence.txt中  



