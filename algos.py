import matplotlib.pyplot as plt
import math
import sys
from gen_data import *


def graham_scan(points):
    #https://gist.github.com/tixxit/242402
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
                hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    def convex_hull(points):
        """Returns points on convex hull of an array of points in CCW order."""
        points = sorted(points)
        l = reduce(_keep_left, points, [])
        u = reduce(_keep_left, reversed(points), [])
        return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

    return convex_hull(points)

def jarvis_march(points):
    #https://gist.github.com/tixxit/252222
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def turn(p, q, r):
        """Returns -1, 0, 1 if p,q,r forms a right, straight, or left turn."""
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _dist(p, q):
        """Returns the squared Euclidean distance between p and q."""
        dx, dy = q[0] - p[0], q[1] - p[1]
        return dx * dx + dy * dy

    def _next_hull_pt(points, p):
        """Returns the next point on the convex hull in CCW from p."""
        q = p
        for r in points:
            t = turn(p, q, r)
            if t == TURN_RIGHT or t == TURN_NONE and _dist(p, r) > _dist(p, q):
                q = r
        return q

    def convex_hull(points):
        """Returns the points on the convex hull of points in CCW order."""
        hull = [min(points)]
        for p in hull:
            q = _next_hull_pt(points, p)
            if q != hull[0]:
                hull.append(q)
        return hull

    return convex_hull(points)

def chans(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def turn(p, q, r):
        """Returns -1, 0, 1 if p,q,r forms a right, straight, or left turn."""
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _dist(p, q):
        """Returns the squared Euclidean distance between p and q."""
        dx, dy = q[0] - p[0], q[1] - p[1]
        return dx * dx + dy * dy


    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
                hull.pop()
        return (not len(hull) or hull[-1] != r) and hull.append(r) or hull

    def _graham_scan(points):
        """Returns points on convex hull of an array of points in CCW order."""
        points.sort()
        lh = reduce(_keep_left, points, [])
        uh = reduce(_keep_left, reversed(points), [])
        return lh.extend(uh[i] for i in xrange(1, len(uh) - 1)) or lh

    def _rtangent(hull, p):
        """Return the index of the point in hull that the right tangent line from p
        to hull touches.
        """
        l, r = 0, len(hull)
        l_prev = turn(p, hull[0], hull[-1])
        l_next = turn(p, hull[0], hull[(l + 1) % r])
        while l < r:
            c = (l + r) / 2
            c_prev = turn(p, hull[c], hull[(c - 1) % len(hull)])
            c_next = turn(p, hull[c], hull[(c + 1) % len(hull)])
            c_side = turn(p, hull[l], hull[c])
            if c_prev != TURN_RIGHT and c_next != TURN_RIGHT:
                return c
            elif c_side == TURN_LEFT and (l_next == TURN_RIGHT or
                                          l_prev == l_next) or \
                    c_side == TURN_RIGHT and c_prev == TURN_RIGHT:
                r = c               # Tangent touches left chain
            else:
                l = c + 1           # Tangent touches right chain
                l_prev = -c_next    # Switch sides
                l_next = turn(p, hull[l], hull[(l + 1) % len(hull)])
        return l

    def _min_hull_pt_pair(hulls):
        """Returns the hull, point index pair that is minimal."""
        h, p = 0, 0
        for i in xrange(len(hulls)):
            j = min(xrange(len(hulls[i])), key=lambda j: hulls[i][j])
            if hulls[i][j] < hulls[h][p]:
                h, p = i, j
        return (h, p)

    def _next_hull_pt_pair(hulls, pair):
        """
        Returns the (hull, point) index pair of the next point in the convex
        hull.
        """
        p = hulls[pair[0]][pair[1]]
        next = (pair[0], (pair[1] + 1) % len(hulls[pair[0]]))
        for h in (i for i in xrange(len(hulls)) if i != pair[0]):
            s = _rtangent(hulls[h], p)
            q, r = hulls[next[0]][next[1]], hulls[h][s]
            t = turn(p, q, r)
            if t == TURN_RIGHT or t == TURN_NONE and _dist(p, r) > _dist(p, q):
                next = (h, s)
        return next

    def convex_hull(pts):
        """Returns the points on the convex hull of pts in CCW order."""
        for m in (1 << (1 << t) for t in xrange(len(pts))):
            hulls = [_graham_scan(pts[i:i + m]) for i in xrange(0, len(pts), m)]
            hull = [_min_hull_pt_pair(hulls)]
            for throw_away in xrange(m):
                p = _next_hull_pt_pair(hulls, hull[-1])
                if p == hull[0]:
                    return [hulls[h][i] for h, i in hull]
                hull.append(p)

    return convex_hull(points)

def quick_hull(sample):
    link = lambda a,b: np.concatenate((a,b[1:]))
    edge = lambda a,b: np.concatenate(([a],[b]))

    def dome(sample,base): 
        h, t = base
        dists = np.dot(sample-h, np.dot(((0,-1),(1,0)),(t-h)))
        outer = np.repeat(sample, dists>0, axis=0)
        
        if len(outer):
            pivot = sample[np.argmax(dists)]
            return link(dome(outer, edge(h, pivot)),
                        dome(outer, edge(pivot, t)))
        else:
            return base

    if len(sample) > 2:
        axis = [x[0] for x in sample]
        base = np.take(sample, [np.argmin(axis), np.argmax(axis)], axis=0)
        return link(dome(sample, base),
                    dome(sample, base[::-1]))
    else:
        return sample


