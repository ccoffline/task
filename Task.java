package pers.ccoffline.task;

import java.util.concurrent.atomic.AtomicInteger;

public class Task<R> {
    private R ret;

    private AtomicInteger status;

    private static final int INIT = 0;
    private static final int READY = 1;
    private static final int RUNNING = 2;
    private static final int FINISHED = 3;
    private static final int ERROR = 4;

    public boolean isReady() {
        return status.get() == READY;
    }
}
