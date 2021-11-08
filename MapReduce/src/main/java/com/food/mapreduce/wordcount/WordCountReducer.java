package com.food.mapreduce.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

/**
 * KEYIN, reduce阶段输入的key类型：LongWriteable
 * VALUEIN, reduce阶段输入value类型：Text
 * KEYOUT， reduce阶段输出的key类型：Text
 * VALUEOUT，reduce阶段输出的value类型：IntWriteable
 */

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable outV = new IntWritable();
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int sum = 0;
        // 累加
        for (IntWritable value : values) {
            sum += value.get();
        }
        outV.set(sum);

        // 写出
        context.write(key, outV);
    }
}
