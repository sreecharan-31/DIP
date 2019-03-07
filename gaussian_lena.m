lena=imread("lena512color.tiff");
lena_gray=rgb2gray(lena);
lena_gray_d=im2double(lena_gray);
var=0.05;
n=size(lena_gray_d);
lena_noisy=cell(100,1);
lena_avg=zeros(n);
for i =1:100
    lena_noisy{i}=lena_gray_d + (sqrt(var)*randn(size(lena_gray_d)));
    lena_avg=lena_avg+lena_noisy{i};
end

imshow(lena_avg/100);
figure;
imshow(lena_gray_d);

