import SecurityNow_Class
import DownloadURL


def main():
    # initialize variables
    sn = SecurityNow_Class.SecurityNow()
    dw = DownloadURL.DownloadURL()
    failed = ['']

    try:
        no_of_ep = int(input('Download to Episode: '))
        trans = input('Download Transcripts: ').lower()
        notes = input('Download Notes: ').lower()
    except ValueError:
        print('Number Please for Episode')
        exit(0)

    # verify input
    if ('y' != trans[0]) and ('n' != trans[0]):
        print('Invalid input one entry.\n\tTranscript should be yes/ no.')
        exit(0)
    elif trans[0] == 'y':
        trans = True
    elif trans[0] == 'n':
        trans = False

    if ('y' != notes[0]) and ('n' != notes[0]):
        print('Invalid input one entry.\n\tNotes should be yes/ no.')
        exit(0)
    elif notes[0] == 'y':
        notes = True
    elif notes[0] == 'n':
        notes = False

    # download the episode
    for ep in range(sn.get_next_ep(), int(no_of_ep)+1):
        print('Episode ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
        dw.set_url(sn.get_url_for_next_ep().get('audio')[0])
        downloaded = dw.download_save(sn.get_url_for_next_ep().get('audio')[1])
        if downloaded:
            print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC, flush=True)
            if trans:
                print('Transcript ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
                dw.set_url(sn.get_url_for_next_ep().get('transcript')[0])
                downloaded = dw.download_save(sn.get_url_for_next_ep().get('transcript')[1])
                if downloaded:
                    print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC, flush=True)
                else:
                    print(DownloadURL.BColors.FAIL + 'Failed.' + DownloadURL.BColors.ENDC, flush=True)
                    # TODO-me FIX failed.append
                    # failed.append(sn.get_url_for_next_ep().get(['transcript']))
            if notes:
                print('Notes ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
                dw.set_url(sn.get_url_for_next_ep().get('notes')[0])
                downloaded = dw.download_save(sn.get_url_for_next_ep().get('notes')[1])
                if downloaded:
                    print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC, flush=True)
                else:
                    print(DownloadURL.BColors.FAIL + 'Failed.' + DownloadURL.BColors.ENDC, flush=True)
                    # TODO-me FIX failed.append
                    # failed.append(sn.get_url_for_next_ep().get(['notes']))
        else:
            print(DownloadURL.BColors.FAIL + 'Failed.' + DownloadURL.BColors.ENDC, flush=True)
            # TODO-me FIX failed.append
            # failed.append(sn.get_url_for_next_ep().get(['audio']))
        sn.update_current()
        sn.write_log()
    print("All Episodes Downloaded.")
    print()


if __name__ == '__main__':
    main()
