Name:		texlive-scientific-thesis-cover
Version:	47923
Release:	1
Summary:	Provides cover page and affirmation at the end of a thesis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scientific-thesis-cover
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scientific-thesis-cover.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Institutions require a cover page and an affirmation at the end
of a thesis. This package provides both.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/scientific-thesis-cover
%{_texmfdistdir}/tex/latex/scientific-thesis-cover
%doc %{_texmfdistdir}/doc/latex/scientific-thesis-cover

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
