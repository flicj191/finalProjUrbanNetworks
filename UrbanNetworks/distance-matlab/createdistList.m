%adjlist
fileID = fopen('textdistance.txt', 'a');
path = './test/'; 
bmatfolder = dir('test');
for i = 3:numel(bmatfolder)
    Ax = importdata(strcat(path,bmatfolder(i).name), ' ');
    [~,namei,~] = fileparts(bmatfolder(i).name); 
    for j = 3:numel(bmatfolder)
        Ay = importdata(strcat(path,bmatfolder(j).name),' ');
        [~,namej,~] = fileparts(bmatfolder(j).name);
        D = B_Distance(Ax,Ay);
        fprintf(fileID, '%s %s %f \n',namei,namej,D ); %fileID open
    end
end

%append to file --adjacency list
 fclose(fileID);