package com.food.mapreduce.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * KEYIN, map阶段输入的key类型：LongWriteable
 * VALUEIN, map阶段输入value类型：Text
 * KEYOUT， map阶段输出的key类型：Text
 * VALUEOUT，map阶段输出的value类型：IntWriteable
 */



public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private Text outK = new Text();
    private IntWritable outV = new IntWritable(1);
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        // 1 获取一行
        // line
        String line = value.toString();
        
        // 2 切割
        String[] words = line.split(" ");

        for (String word : words) {
            // 封装outk
            outK.set(word);

            // 写出
            context.write(outK, outV);
        }

    }
}









