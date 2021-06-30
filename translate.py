#!/usr/bin/env python
# coding=UTF-8

import os
import sys
import re
import argparse
import pprint
import csv
import json

#not implemented right now
name_dict = {
    # In VNDB Character list order
    # Protagonists
    '羽咲': 'Hasaki',
    '卓司': 'Takuji',
    '皆守': 'Tomosane',
    '由岐': 'Yuki',
    'ざくろ': 'Zakuro',
    # Main Characters
    '彩名': 'Ayana',
    '希実香': 'Kimika',
    '鏡': 'Kagami',
    '司': 'Tsukasa',
    # Side Characters
    'めぐ': 'Megu',
    '飯沼': 'Iinuma',
    '美羽': 'Miu',
    '木村': 'Kimura',
    '聡子': 'Satoko',
    '清川': 'Senagawa',
    '明日美': 'Asumi',
    'マスター': 'Master',
    '水上': 'Minakami',
    '西村': 'Nishimura',
    '沼田': 'Numada',
    'リルル': 'Riruru',
    '瀬名川': 'Senagawa',
    '城山': 'Shiroyama',
    '潔': 'Kiyoshi',
    'やす子': 'Yasuko',
    # Makes an appearance
    '飯田': 'Iida',
    '浩夫': 'Hiroo',
    '亜由美': 'Ayumi',
    '琴美': 'Kotomi',
    '母親': 'Mother',
    '宇佐美': 'Usami',
    # Not on VNDB
    'アリス': 'Alice',
    '共同（司・鏡）': 'Kagami+Tsukasa',
    'うさぎ': 'Rabbit',
    '本': 'Book',
    'くま': 'Bear',
    'おっさん': 'Man',
    '女子校生': 'Female Student',
    '男子校生': 'Male Student',
    '教師': 'Teacher',
    'タレブさん': 'Taleb-san',
    '校内放送': 'Announcement',
    'おばさん': 'Woman',
    '生田': 'Ikuta',
    '川端': 'Kawabata',
    '田村': 'Tamura',
    '島田': 'Shimada',
    '時坂': 'Tokisaka',
    '不安': 'Anxiety',
    '明日美の父': 'Asumi\'s Dad',
    '明日美の母': 'Asumi\'s Mom',
    'おばちゃん': 'Older Woman',
    '男性の通行人': 'Male Pedestrian',
    '女性の通行人': 'Female Pedestrian',
    '会社員': 'Office Worker',
    '観衆': 'Onlookers',
    '男性店員': 'Male Staff',
    '年配の男性教師': 'Elderly Male Teacher',
    '女性教師': 'Female Teacher',
    '他校生徒': 'Student from Another School',
    '不良達': 'Delinquents',
    '神': 'God',
    '悪しき者': 'Evil Person',
    'オカマ': 'Homosexual',
    '練習生': 'Dojo Student',
    '渡辺': 'Watanabe',
}

def get_fnames():
    ret = []
    for root, dir, file in os.walk('txt_scripts_jp'):
        for fname in file:
            if fname != ".gitkeep":
                ret.append(os.path.join(root, fname))
    return ret

def create_translation_csv(outname=''):
    total_lines = []
    fnames = get_fnames()
    for fname in fnames:
        print("Reading "+str(fname)+"...")
        with open(fname, 'r', encoding='utf8') as f:
            scriptline = f.readline()
            line_num = 0
            while scriptline:

                new_line = re.sub(r'^\<\d*\>', "", scriptline).rstrip()

                if new_line not in files:
                    total_lines.append((new_line, line_num, fname))

                line_num = line_num + 1
                scriptline = f.readline()

    print('Total number of lines: {}'.format(len(total_lines)))

    with open(outname, 'w', encoding='utf8') as csvfile:
        print("Writing lines...")
        csvwriter = csv.writer(csvfile)
        for line, line_num, fname in total_lines:
            csvwriter.writerow([line, line, line_num, fname])
        print("Complete!")

def create_translation_scripts():
    translation = {}
    fnames = get_fnames()
    for fname in fnames:
        fshort = os.path.split(fname)[1]
        new_key = fshort[:len(fshort)-4]
        translation[new_key] = {}

    with open('translation.csv', 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            fshort = os.path.split(row[3])[1]
            new_key = fshort[:len(fshort)-4]
            translation[new_key][row[2]] = row[1]

    en_files = []
    for file in translation:
        fname = os.path.join('txt_scripts_jp', str(file)+".txt")
        outname = os.path.join('txt_scripts_en', str(file)+".txt")
        with open(outname, 'w', encoding='utf8') as en_f:
            with open(fname, 'r', encoding='utf8') as jp_f:
                line_num = 0
                jp_scriptline = jp_f.readline()
                while jp_scriptline:
                    ln = str(line_num)
                    if ln in translation[file].keys():
                        eng_line = translation[file].pop(ln)
                        new_line = "<"+ln+">"+eng_line
                    else:
                        new_line = jp_scriptline.rstrip()

                    en_f.write(new_line+'\n')
                    #print(new_line)

                    line_num+=1
                    jp_scriptline = jp_f.readline()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--make_csv', help='File to save empty translation csv', default='',
                        type=str)
    parser.add_argument('--make_translation_scripts', help='use translation.csv to rewrite scripts',
                        action='store_true', default=False)
    args = parser.parse_args()

    print('Arguments:\n{}\n'.format(' '.join(sys.argv[1:])))

    print('Config:')
    pprint.pprint(vars(args), depth=2, width=50)

    with open('files.json', encoding="utf8") as o:
        files = json.load(o)

    if args.make_csv:
        create_translation_csv(outname=args.make_csv)
    if args.make_translation_scripts:
        create_translation_scripts()
