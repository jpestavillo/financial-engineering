function [Exactitud, Precision, Recall] = desempenio(Yhat,Y)
% Funci�n que da como resultado la exactitud, precision y recall de los
% datos estimados vs los datos reales. Recibe �nicamente datos binarios. 

conf = confusionmat(Yhat,Y);

tn = conf(1);
fn = conf(3);
fp = conf(2);
tp = conf(4);

Exactitud = (tp + tn)/(tp+tn+fp+fn);
Precision = tp/(tp+fp);
Recall = tp/(tp+fn);
end
